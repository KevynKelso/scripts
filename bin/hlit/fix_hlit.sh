#!/bin/bash

lesson_num=5

for step_num in {1..7}; do
    branch_name=$(printf "fix/content_l%d_s%d" $lesson_num $step_num)
    git checkout $branch_name
    find . -regex ".*lesson-$lesson_num.*step-$step_num.*\.tsx" | xargs nvim
    git add .
    git commit -m "fix(pages): format files"
    git push -u origin $branch_name
done

