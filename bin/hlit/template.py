STUDENT_TEMPLATE = '''import React from "react";
import ContentWrapper from "~/components/ContentWrapper";
import H1 from "~/components/Typography/H1";
import LessonLayout from "~/layouts/lesson";

const Page = () => {
  return (
      <LessonLayout
        current_step={$current_step}
        lesson={"Lesson $lesson_number"}
        color={"$name"}
        total_count={$total_steps}
        module_title={undefined}
      >
        <ContentWrapper>
          $content
        </ContentWrapper>
      </LessonLayout>
  )
}

export default Page;

'''
INSTRUCTOR_TEMPLATE = '''import React, { useState } from "react";
import ContentWrapper from "~/components/ContentWrapper";
import H1 from "~/components/Typography/H1";
import LessonLayout from "~/layouts/lesson";
import TeacherViewWrapper from "~/layouts/teacher-view-wrapper";
import { Indent } from '~/content/styledComponents.tsx';
import { StudentCard, TeacherCard } from "~/components/content-card";

const Page = () => {
  const [studentFullScreen, setStudentFullScreen] = useState<boolean>(false);
  const [teacherFullScreen, setTeacherFullScreen] = useState<boolean>(false);

  return (
      <LessonLayout
        current_step={$current_step}
        lesson={"Lesson $lesson_number"}
        color={"$name"}
        total_count={$total_steps}
        module_title={undefined}
      >
        <ContentWrapper>
          $step_content

          <TeacherViewWrapper>
            <StudentCard
              fullScreen={studentFullScreen}
              hidden={teacherFullScreen}
              highSchool={true}
              setFullScreen={setStudentFullScreen}
            >
              $student_content
            </StudentCard>
            <TeacherCard
              fullScreen={teacherFullScreen}
              hidden={studentFullScreen}
              highSchool={true}
              setFullScreen={setTeacherFullScreen}
            >
              $teacher_content
            </TeacherCard>
          </TeacherViewWrapper>
        </ContentWrapper>
      </LessonLayout>
  )
}

export default Page;

'''
