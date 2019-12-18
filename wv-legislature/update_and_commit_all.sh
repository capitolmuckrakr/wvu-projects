#!/bin/bash

scrape_and_commit () {
    python agency_reports.py
    local csv="*.csv"
    local commit_txt="all_reports.commit.txt"
    git add $csv
    git commit -F $commit_txt && \
        git push -q https://${GITHUB_PERSONAL_TOKEN}@github.com:dwillis/wvu-projects.git master \
        || true
}

git config --global user.email "wvu_projects@example.com"
git config --global user.name "WVU Projects"

scrape_and_commit
