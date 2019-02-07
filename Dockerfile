FROM python:3.7.2-slim

LABEL "name"="filter"
LABEL "maintainer"="OwnersRoom <hello@ownersroom.com>"
LABEL "version"="1.0.0"

LABEL "com.github.actions.name"="OwnersRoom Actions"
LABEL "com.github.actions.description"="Actions used by OwnersRoom"
LABEL "com.github.actions.icon"="eye"
LABEL "com.github.actions.color"="blue"

COPY entrypoint.sh filters LICENCE README.md /

ENTRYPOINT ["/entrypoint.sh"]
