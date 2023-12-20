package main

import (
	"archive/zip"
	"fmt"
	"io"
	"log"
	"os"
	"strings"
)

func unzipArchive(path string) {
	fmt.Printf("Absolute path to zip archive: %s\n", path)
	ts := strings.Split(path, "/")
	len_ts := len(ts)
	fmt.Printf("Opening archive: %s\n", ts[len_ts-1])

	r, err := zip.OpenReader(path)
	if err != nil {
		log.Fatalf("Error: Unable to open zip file.\n %s\n", err)
	}
	defer r.Close()

	fmt.Println("-----------------------------")

	for _, f := range r.File {
		if f.FileInfo().IsDir() {
			fmt.Printf("Creating folder: %s\n", f.Name)
			if err := os.Mkdir(f.Name, os.ModePerm); err != nil {
				log.Fatalf("Error: Unable to create directory\n%s\n", err)
			}
			continue
		} else {
			fmt.Printf("Inflating file: %s\n", f.Name)
			rc, err := f.Open()
			if err != nil {
				log.Fatalf("impossible to open file n°%s in archive: %s", f.Name, err)
			}
			defer rc.Close()
			uCFile, err := os.Create(f.Name)
			if err != nil {
				log.Fatalf("Error creating uncompressed file: %s\n", err)
			}
			_, err = io.Copy(uCFile, rc)
			if err != nil {
				log.Fatalf("Error while inflating file: %s\n", err)
			}
		}
	}
}
