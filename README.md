# Old_man_Assignment3
-----
**Members**
1. คณิสร เข็มทอง 6030064821
2. วชิรฉัตร สวัสดิวัตน์ ณ อยุธยา 6030506921
3. ธียศ ศิริเสรีวรรณ 6031027821
4. นนทกร เกตุนิรัตน์ 6031028421
5. นนทกร ตะบูนพงศ์ 6031029021
-----
**Answer**

Q1 เราต้อง concern เรื่องการ code แต่ละส่วนควรทำงานแยกกัน เช่น layer view ก้ควรมีแค่ code ที่ทำงานแค่ view ของโปรแกรม ส่วน controller ก็ควรจะทำงานเพียงแค่ในส่วนของ controller โดยแต่ละอันจะเรียกผ่าน function หรือ interface ของกันและกัน

Q2 ไม่ได้ เพราะไม่มีตัวช่วยในการคุมการแสดง presentation layer ถ้าเกิด business logic เปลี่ยนก็จะทำให้ข้อมูลใน persentation layer เปลี่ยนไปเลย ดังนั้นเราควรเติมตัว controller เพิ่มช่วยในการควบคุม การทำงานของ presentation

Q3 เติมโค้ดส่วนนี้เข้าไปเพื่อให้ครบ layer
<br />
<img src='/Resource/Q3.jpeg'>

Q4 เติมโค้ดส่วนนี้เข้าไปเพื่อให้ครบ layer

<img src='/Resource/Q4.jpeg'>

Q5 ทำหน้าที่ในการ control model ต่างๆ ที่ถูกเรียกใช้ใน layer ของ controller จัดการเรื่อง model ต่างๆ

Q6 ข้อดีของ model mvc คือเมื่อเราแยก layer เป็น 3 ชั้นแล้วทำให้การทำงานในแต่ละชั้น dependency ต่อกันเมื่อแก้ไข logic หรือ view ในชั้นใดชั้นหนึ่งก็จะไม่กระทบกับชั้นอื่นๆ เมื่อไม่กระทบก็ทำให้ระบบดูง่ายไม่ซับซ้อนส่งผลให้การแก้ไขส่วนต่างๆ เป็นไปได้ง่าย แต่ข้อเสียของระบบนี้คือเมื่อมีโค้ดมากขึ้นวุ่นวายขึ้นก็จะ maintain ได้ยากขึ้นไปอีก เพราะ code จะไปเพิ่มแค่ในตัวของ controller เยอะๆเท่านั้น และตัวของ controller ยึดติดกับส่วนของ view มากเกินไป

Q7 

<img src='/Resource/Q7.jpeg'>

Q8 เพื่อทำการลด Dependency ระหว่าง Object และทำ Polymorphism

Q9 Presenter จะทำหน้าที่รับ Event ที่ได้มาจาก View ได้แก่ Add Note, Get All Note และ Clear Note แล้วอัพเดท View และ Model

Q10 MainController เป็นแค่ Interface ที่เอาไว้บอกว่า Presenter จะมีฟังก์ชันใดที่ต้อง Implement บ้าง ส่วน Method ใน MainPresenter จะเป็น Method ที่ Implement จาก Interface เรียบร้อยแล้ว และจะใช้เป็นสื่อกลางในการอัพเดท View และ Model

Q11 View มีปฏิสัมพันธ์กับ Presenter โดยการที่ View จะไปเรียกให้ Presenter ทำฟังก์ชันต่างๆแล้วมาอัพเดต View โดย View จะไม่อัพเดตตัวเอง

Q12 

<img src='/Resource/Q12.jpg'>

Q13 เทียบกับ MVC แล้ว MVP จะแบ่งแยก Model กับ View ได้อย่างชัดเจนมากกว่า แต่ข้อเสียเมื่อเทียบกับ MVC คือ จำนวนโค้ดที่เขียนจะมีมากกว่า เพราะต้องเขียนรองรับทุกการกระทำที่เกิดจาก View และยังต้องเขียน Code รองรับการกระทำที่เกิดขึ้นเพื่อส่งข้อมูลกลับไปแสดงยัง View อีกรอบด้วย

Q14 Testable มากขึ้น เพราะมี Dependencies ที่เป็น Abstract

Q15 It is a programming paradigm concerned with data streams and the propagation of change.

Q16 The observer pattern is a software design pattern in which an object, called the subject, maintains a list of its dependents, called observers, and notifies them automatically of any state changes, usually by calling one of their methods.

Q17 Not necessary, as the view is the only component required to acknowledge data change

Q18 Using BehaviorSubject, which can reference the value in real time and observed by the observer.

Q19 self.note_behavior_subject.on_next(self.note_repository.get_all_notes())

Q20 ViewModel detects change in View, then process accordingly, and vice versa.

Q21 The Presenter must update itself, while the ViewModel does not.

Q22 ViewModel, as reference is not necessary.

Q23 By calling the ViewModel method with input parameter.

Q24

<img src='/Resource/Q24.png'>

Q25 MVVM runs single page application faster, while consuming more memory via data binding

Q26 MVC, as this pattern is the simplest and suitable for a lower scale project.