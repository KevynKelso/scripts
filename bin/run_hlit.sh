#!/bin/bash

lesson_num=5

for step_num in {1..7}; do
    branch_name=$(printf "fix/content_l%d_s%d" $lesson_num $step_num)
    echo $branch_name
    git checkout main
    git pull
    git checkout -b $branch_name
    hlit_content_verification.py $lesson_num $step_num
    hlit_dx.py $lesson_num $step_num
    git add .
    git commit -m "fix(pages): lesson $lesson_num step $step_num content verification"
    gh pr create --title "fix(pages): lesson $lesson_num step $step_num content verification" --body "## Changes\n- lesson $lesson_num step $step_num content verification" -w
    git push -u origin $branch_name
done
