#include <zip.h>
#include <string>
#include <vector>
#include <sys/stat.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>

void safe_create_dir(const char *dirName)
{
    if (mkdir(dirName, 0755) < 0) {
        if (errno != EEXIST) {
            perror(dirName);
            exit(1);
        }
    }
}

int inflate(const char *srcPath, const char *destPath)
{
    const char *archive = srcPath;
    struct zip *za;
    struct zip_file *zf;
    struct zip_stat sb;
    char buffer[100];
    int err;
    int i, len;
    int fd;
    long long sum;

    if ((za = zip_open(archive, 0, &err)) == NULL) {
        zip_error_t error;
        zip_error_init_with_code(&error, err);
        fprintf(stderr, "Cannot open zip archive '%s': %s\n",
	        archive, zip_error_strerror(&error));
        zip_error_fini(&error);
        return -1;
    }

    if (destPath != "") {
        chdir(destPath);
    }
    
    for (i = 0; i < zip_get_num_entries(za, 0); i++) {
        if (zip_stat_index(za, i, 0, &sb) == 0) {
            len = strlen(sb.name);
            if (sb.name[len - 1] == '/') {
                safe_create_dir(sb.name);
            } else {
                zf = zip_fopen_index(za, i, 0);
                if (!zf) {
                    fprintf(stderr, "boese, boese\n");
                    exit(100);
                }
 
                fd = open(sb.name, O_RDWR | O_TRUNC | O_CREAT, 0644);
                if (fd < 0) {
                    fprintf(stderr, "boese, boese\n");
                    exit(101);
                }
 
                sum = 0;
                while (sum != sb.size) {
                    len = zip_fread(zf, buffer, 100);
                    if (len < 0) {
                        fprintf(stderr, "boese, boese\n");
                        exit(102);
                    }
                    write(fd, buffer, len);
                    sum += len;
                }
                close(fd);
                zip_fclose(zf);
            }
        } else {
            printf("File[%s] Line[%d]\n", __FILE__, __LINE__);
        }
    }   
 
    if (zip_close(za) == -1) {
        fprintf(stderr, "Can't close zip archive `%s'\n", archive);
        return 1;
    }
    return 0;
}