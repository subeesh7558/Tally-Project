import os
from re import I
from tkinter import ttk
from tkinter import *
from turtle import width

root=Tk()
root.title("Window")
root.geometry("1520x720+0+0")
root.resizable(0,0)
root.configure(background="white")


l2=Label(root,text="c-name",font=("times new roman",13,"bold"),bg="blue",fg="white",relief=GROOVE,bd=5)
l2.grid(row=0,column=1,ipadx=600,sticky=W)
bt1=Button(root,text="print",font=("times new roman",11,"bold"),bg="blue",fg="white",command=root.destroy,relief=GROOVE,bd=2)
bt1.grid(row=0,column=2,ipadx=100,)

f0=Frame(root,height=650,width=180,bg="white",relief=RAISED,bd=5)
f0.place(x=1322,y=35,width=195,height=650)

cmb=ttk.Combobox(f0 ,values="",font=("times new roman",10,"bold"))
cmb.pack(fill=X,pady=2,padx=2)

index_frame=Frame(root,bg="white",relief=RAISED,bd=5)
index_frame.place(x=10,y=35,width=1300,height=650)
f1=Frame(index_frame,height=650,width=1200,bg="white",relief=RAISED,bd=5)
f1.place(x=450,y=155,width=400,height=400)

def Stock_group_analysis():
        f1.destroy()
        l2.destroy()
        l5.destroy()
        l11=Label(root,text="c-name",font=("times new roman",13,"bold"),bg="blue",fg="white",relief=GROOVE,bd=5)
        l11.grid(row=0,column=1,ipadx=500,sticky=W)
        l1=Label(root,text="Select stock group analysis",font=("times new roman",13,"bold"),bg="blue",fg="white",relief=GROOVE,bd=5)
        l1.grid(row=0,column=0,ipadx=10,)


        f0=Frame(index_frame,height=100,width=1200,bg="white",relief=RIDGE,bd=1)
        f0.place(x=550,y=65,width=200,height=100)

        f0_l0=Label(f0,text="Name of group",font=("times new roman",15,"bold"),bg="blue",fg="white")
        f0_l0.pack(fill=X,pady=2) 

        options_list = ["Option 1", "Option 2", "Option 3", "Option 4"]
        value_inside = StringVar(index_frame)
        
        value_inside.set("Select an Option")
        
        

        cmb=ttk.Combobox(f0,values=options_list,font=("times new roman",10,"bold"))
        cmb.pack(fill=X,pady=2,padx=2)

        sgaf1=Frame(index_frame,height=100,width=1200,bg="white",relief=RIDGE,bd=5)
        sgaf1.place(x=470,y=200,width=350,height=400)



        f1_l0=Label(sgaf1,text="List of Stock groups",font=("times new roman",12,"bold"),bg="blue",fg="white")
        f1_l0.pack(fill=X,pady=2,padx=2)
        bt0=Button(sgaf1,text="group1",font=("times new roman",12,"bold"),bg="white",fg="red",command=selected_groups)
        bt0.pack(fill=X,pady=2,padx=2)
        bt1=Button(sgaf1,text="  group2",font=("times new roman",12,"bold"),bg="white",fg="red",command=lambda:os.system("python3 Stock Group Analysis.py"))
        bt1.pack(fill=X,pady=2,padx=2)
        bt2=Button(sgaf1,text="group3",font=("times new roman",12,"bold"),bg="white",fg="red",command=lambda:os.system("python3 Stock Group Analysis.py"))
        bt2.pack(fill=X,pady=2,padx=2)
        bt3=Button(sgaf1,text="group4",font=("times new roman",12,"bold"),bg="white",fg="red",command=lambda:os.system("python3 Stock Group Analysis.py"))
        bt3.pack(fill=X,pady=2,padx=2)
def selected_groups():
        f1.destroy()
        l2.destroy()
        l5.destroy()
        cmb.destroy()

        index_frame.destroy()
        l1=Label(root,text="Stock group analysis",font=("times new roman",13,"bold"),bg="blue",fg="white",relief=GROOVE,bd=5)
        l1.grid(row=0,column=0,ipadx=35,)

        options_list=["Period","Stock Category Analysis","Stock Item Analysis"]
        cm=ttk.Combobox(f0 ,values=options_list,font=("times new roman",10,"bold"))
        cm.pack(fill=X,pady=2,padx=2)
        cm.current(0)
        selected_groups_frame=Frame(root,bg="white",relief=RAISED,bd=2)
        selected_groups_frame.place(x=10,y=35,width=1300,height=650)

        f11=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=2)
        f11.grid(row=1,column=0,columnspan=3,ipadx=200)
        l1f1=Label(f11,text="Perticulars",font=("times new roman",12,"bold"),bg="blue",fg="white",borderwidth=5,relief=GROOVE,width=20,height=6)
        l1f1.pack(fill=X,pady=2,padx=2)
        f12=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=2)
        f12.place(x=610,y=0,width=680,height=80)
        l1f2=Label(f12,text="PRODUCT NAME",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
        l1f2.place(x=305,y=10,anchor="center")
        l1f3=Label(f12,text="C NAME",font=("times new roman",9,"bold"),bg="white",fg="black")
        l1f3.place(x=305,y=30,anchor="center")
        l1f4=Label(f12,text="FOR 1-APR-20",font=("times new roman",9,"bold"),bg="white",fg="black")
        l1f4.place(x=305,y=50,anchor="center")

        f13=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=2)
        f13.place(x=0,y=145,width=607,height=450)
        f13bt1=Button(f13,text="PRODUCT-1",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        f13bt1.place(x=0,y=0,anchor="nw")
        f13bt2=Button(f13,text="PRODUCT-2",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        f13bt2.place(x=0,y=30,anchor="nw")
        f13bt3=Button(f13,text="PRODUCT-3",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        f13bt3.place(x=0,y=60,anchor="nw")
        f13bt4=Button(f13,text="PRODUCT-4",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        f13bt4.place(x=0,y=90,anchor="nw")

        f14=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
        f14.place(x=610,y=83,width=340,height=58)
        l1f5=Label(f14,text="INWARDS",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
        l1f5.place(x=0,y=0,anchor="nw")
        l1f6=Label(f14,text="Quantity",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l1f6.place(x=0,y=30,anchor="nw")
        l1f7=Label(f14,text="Eff.Rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l1f7.place(x=80,y=30,anchor="nw")
        l1f8=Label(f14,text="Value",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l1f8.place(x=180,y=30,anchor="nw")



        f15=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
        f15.place(x=950,y=83,width=340,height=58)
        l2f5=Label(f15,text="OUTWARDS",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
        l2f5.place(x=0,y=0,anchor="nw")
        l2f6=Label(f15,text="Quantity",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l2f6.place(x=0,y=30,anchor="nw")
        l2f7=Label(f15,text="Eff.Rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l2f7.place(x=80,y=30,anchor="nw")
        l2f8=Label(f15,text="Value",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l2f8.place(x=180,y=30,anchor="nw")

        f16=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=2)
        f16.place(x=610,y=145,width=340,height=450)
        l3f6=Label(f16,text="10 Nos",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l3f6.place(x=0,y=0,anchor="nw")
        l3f7=Label(f16,text="10",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l3f7.place(x=80,y=0,anchor="nw")
        l3f8=Label(f16,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l3f8.place(x=180,y=0,anchor="nw")
        

        f17=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=2)
        f17.place(x=950,y=145,width=340,height=450)
        l4f6=Label(f17,text="10 Nos",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l4f6.place(x=0,y=0,anchor="nw")
        l4f7=Label(f17,text="10",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l4f7.place(x=80,y=0,anchor="nw")
        l4f8=Label(f17,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l4f8.place(x=180,y=0,anchor="nw")


       
        f18=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=2)
        f18.place(x=0,y=598,width=607,height=48)
        l5f6=Label(f18,text="Total",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l5f6.place(x=0,y=0,anchor="nw")

        f19=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=2)
        f19.place(x=610,y=598,width=340,height=48)
        l6f6=Label(f19,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l6f6.place(x=0,y=0,anchor="nw")

        f20=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=2)
        f20.place(x=950,y=598,width=340,height=48)
        l7f6=Label(f20,text="100",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l7f6.place(x=0,y=0,anchor="nw")




        







l5=Label(index_frame,text="Movement Analysis",font=("times new roman",25,"bold"),bg="blue",fg="white",)
l5.pack(fill="x")
bt1=Button(f1,text="Stock Group Analysis",font=("times new roman",15,"bold"),bg="blue",fg="white",command=Stock_group_analysis)
bt1.pack(fill="x",padx=10,pady=10)
bt2=Button(f1,text="Stock Category Analysis",font=("times new roman",15,"bold"),bg="blue",fg="white",command=root.destroy)
bt2.pack(fill="x",padx=10,pady=10)
bt3=Button(f1,text="Stock Item Analysis",font=("times new roman",15,"bold"),bg="blue",fg="white",command=root.destroy)
bt3.pack(fill="x",padx=10,pady=10)
bt4=Button(f1,text="Group Analysis",font=("times new roman",15,"bold"),bg="blue",fg="white",command=root.destroy)
bt4.pack(fill="x",padx=10,pady=10)
bt5=Button(f1,text="Exit",font=("times new roman",15,"bold"),bg="blue",fg="white",command=root.destroy)
bt5.pack(fill="x",padx=10,pady=10)





















root.mainloop()
