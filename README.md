# OwnersRoom Github Actions

This action includes filters, among them a file glob pattern filter to stop workflows unless at least one added, changed or removed file pattern matches.

## Available filters

### file

Continue if the event is a tag.

```workflow
action "file-filter" {
  uses = "ownersroom/github-actions@master"
  args = "file src/**/* dist/* ./file.txt"
}
```

## License

The Dockerfile and associated scripts and documentation in this project are released under the [MIT License](LICENSE).
