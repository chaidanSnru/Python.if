# ประกาศ list a มีค่าระหว่าง 2 -20
a = list(range(2,21))
# ประกาศ list b มีค่าระหว่าง 1 -12
b = list(range(1,13))
# ประกาศ list c มีค่า่ว่าง
c = []
# ประกาศ for loop ใช้ตัวแปรเชื่่อมโยง d กับ list a
for d in a:
    # ทำการตรวจสอบตัวแปร d ว่าเป็นเลขคี่หรือเลขคู่
    if d%2 != 0:
    # ประกาศ for loop ใช้ตัวแปรเชื่่อมโยง e กับ list b
        for e in b:
            # ประกาศ f สำหรับเก็บ string ตามสูตรคูณ
            f = str(e) + "x" + str(d) + "=" +str(d*e)
            # เพิ่มค่า f เข้าไปใน list c
            c.append(f)
        # print บอกว่าสูตรคูณแม่ไหนตามค่า d
        print("สูตรคูณแม่ "+str(d)+" คือ")
        # print list c
        print(c)
        # กำหนดให้ list c มีค่าว่าง
        c=[]