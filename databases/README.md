* Last Name: Wong
* First Name: Tiffany

Please see here for [Mini-Lesson #3](https://colab.research.google.com/drive/1QL9iawHP9_PzozoU5Q504uZuIrIqQxql?usp=sharing), which contains both the homework and async work queries.

## Homework
```
    SELECT s.First AS First, s.Last AS Last, s.StudentID AS StudentID, s.ScanTime AS ScanTime, s.Status AS Status, 
    p.Date AS Date, p.CourseSection AS CourseSection, p.Attendance AS Attendance, p.Teacher AS Teacher, p.Period AS Period
    FROM scan AS s
    INNER JOIN periodAtt AS p
    ON s.studentID = p.studentID
    AND substr(ScanTime,1,instr(s.scanTime, ' ')-1) = p.Date
    WHERE p.Attendance = 'A'
    ORDER BY s.Last, s.First ASC
```

## Async Challenge #1
```
    SELECT Teacher, COUNT(Attendance) AS TotalCuts
    FROM (SELECT s.First AS First, s.Last AS Last, s.StudentID AS StudentID, s.ScanTime AS ScanTime, s.Status AS Status, 
    p.Date AS Date, p.CourseSection AS CourseSection, p.Attendance AS Attendance, p.Teacher AS Teacher, p.Period AS Period
    FROM scan AS s
    INNER JOIN periodAtt AS p
    ON s.studentID = p.studentID
    AND substr(ScanTime,1,instr(s.scanTime, ' ')-1) = p.Date
    WHERE p.Attendance = 'A'
    ORDER BY s.Last, s.First ASC) AS allCuts
    GROUP BY Teacher
    ORDER BY TotalCuts DESC
```

## Classwork Resources
Please see below for Mini-Lessons #1 and #2:
* [Completed Google Colab: Mini-Lesson #1](https://colab.research.google.com/drive/1-CthRPMSb9sf84Q0LYuZHRZU3LTFX9I7?usp=sharing)

* [Completed Google Colab: Mini-Lesson #2](https://colab.research.google.com/drive/1CCcRvx6BRCTjj1QyFGdHsddKB1Gcv1SZ?usp=sharing)
  