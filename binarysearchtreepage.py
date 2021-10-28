import time
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
from tkinter.constants import COMMAND


class Node(object):
    def __init__(self,val,canvas,parent=None):
        self.val = val
        self.left = None
        self.right = None
        self.canvas = canvas
        self.parent = parent


class binarysearchtree_contents(object):
    
    def __init__(self,parentframe, width, height):
        self.x = width/2
        self.y = 40
        self.root = None
        self.heading = ttk.Label(master=parentframe,background="#00003f",foreground="#20E61A", text="BINARY SEARCH TREE", font=('Helvetica', 34),)
        self.heading.pack(fill=tk.X, padx=680, pady=30)
        self.set_of_operations = tk.Frame(master=parentframe, padx=40, bg="#00003f")
        s=ttk.Style()
        s.configure('TFrame', background='#00003f')
        self.node = ttk.Entry(master=self.set_of_operations)
        self.node.insert(0, "Enter node value")
        self.node.bind('<Button-1>', self.deletetext)
        self.output_frame = ttk.Frame(master=parentframe)
        # CHANGE CANVAS BG HERE
        self.output = tk.Canvas(master=self.output_frame,bg="#fff",width=1160,height=720, bd=1, highlightthickness=1, highlightbackground="#d8d8d8",relief=tk.FLAT,scrollregion=(0,0,100,100))
        # self.output = tk.Canvas(master=self.output_frame,width=1160,height=520,bg="chocolate",relief=tk.RAISED,bd=8)
        
        # self.output_text=tk.Canvas.create_text(600,700,fill="darkblue",font="Times 20 italic bold",text="")
        self.insert_b = ttk.Button(master=self.set_of_operations, text="INSERT", command=lambda: self.insert(self.output))
        self.search_b = ttk.Button(master=self.set_of_operations, text="SEARCH", command=lambda: self.search(self.output))
        self.delete_b = ttk.Button(master=self.set_of_operations, text="DELETE", command=lambda: self.delete(self.output))
        self.inorder_d = ttk.Button(master=self.set_of_operations, text="INORDER", command=lambda :[self.inorderTraversal(self.root,self.output),self.read()])
        self.preorder_d = ttk.Button(master=self.set_of_operations, text="PREORDER", command=lambda: [self.preorderTraversal(self.root,self.output),self.read()])
        self.postorder_d = ttk.Button(master=self.set_of_operations, text="POSTORDER", command=lambda: [self.postorderTraversal(self.root,self.output),self.read()])
        self.clear_d = ttk.Button(master=self.set_of_operations, text="Clear", command=lambda: self.clearFunc())
        # self.output_text=tk.Canvas.create_text(600,700,fill="darkblue",font="Times 20 italic bold",text=)
        self.allow_execution = True
        self.node.pack(side=tk.LEFT, ipady=4, ipadx=4,padx=(1,10))
        self.insert_b.pack(side=tk.LEFT, padx=2,ipady=4, ipadx=4)
        self.search_b.pack(side=tk.LEFT, padx=2,ipady=4, ipadx=4)
        self.delete_b.pack(side=tk.LEFT, padx=2,ipady=4, ipadx=4)
        self.inorder_d.pack(side=tk.LEFT, padx=2,ipady=4, ipadx=4)
        self.preorder_d.pack(side=tk.LEFT, padx=2,ipady=4, ipadx=4)
        self.postorder_d.pack(side=tk.LEFT, padx=2,ipady=4, ipadx=4)
        self.clear_d.pack(side=tk.LEFT, padx=2,ipady=4, ipadx=4)

        self.set_of_operations.pack()

        # self.horscroll = tk.Scrollbar(master=self.output_frame,orient=tk.HORIZONTAL)
        # self.horscroll.configure(command=self.output.xview)
        # self.horscroll.pack(side=tk.BOTTOM,fill=tk.X)

        # self.verscroll = tk.Scrollbar(master=self.output_frame, orient=tk.VERTICAL)
        # self.verscroll.configure(command=self.output.yview)
        # self.verscroll.pack(side=tk.RIGHT, fill=tk.Y)

        # self.output.configure(yscrollcommand=self.verscroll.set,xscrollcommand=self.horscroll.set)

        self.output.pack( expand=1)
        self.output_frame.pack(pady=20, padx=40, fill=tk.BOTH, expand=1)
        self.output['scrollregion'] = (0, 0,width,height)
        
    

    def insert(self,output):
        # input = int(self.node.get())
        # if input == "" or input == "Enter node value":
        #     msg.showwarning(title="No Input", message="Please enter input")
        #     return
        input = self.node.get()
        if input == "" or input == "Enter node value":
            msg.showwarning(title="No Input", message="Please enter input")
            return
        input=int(input)    
        if not self.root:
            curr_circle = output.create_oval(self.x,self.y,self.x+40,self.y+40,fill="black")
            curr_text = output.create_text(self.x+20,self.y+20,text=input,fill="white")
            canvas = [curr_circle,curr_text,None]
            self.root = Node(input,canvas)
            self.animate(canvas,output)
            return
        temp = self.root
        #Left sub tree from root
        if input<temp.val:

            while temp:
                if input<temp.val:
                    prev = temp
                    self.animate(prev.canvas,output)
                    temp = temp.left
                    if not temp:
                        ancestor = prev.parent
                        if ancestor and ancestor.val <= prev.val:
                            self.move_all_cnodes(prev, 40, output)
                            #output.move(prev.canvas[0], 40, 0)
                            #output.move(prev.canvas[1], 40, 0)
                            #xa, ya, xa1, ya1 = output.coords(ancestor.canvas[0])
                            #xp, yp, xp1, yp1 = output.coords(prev.canvas[0])
                            #output.coords(prev.canvas[2], xa1, ya + 20, xp + 20, yp)
                            #output.update()

                        x, y, x1, y1 = output.coords(prev.canvas[0])
                        arrow = output.create_line(x, y + 20, x - 20, y + 40, arrow=tk.LAST, capstyle=tk.BUTT,
                                                   fill="black")

                        x -= 40
                        y += 40

                        curr_circle = output.create_oval(x, y, x + 40, y + 40, fill="black")
                        curr_text = output.create_text(x + 20, y + 20, text=input, fill="white")
                        canvas = [curr_circle, curr_text, arrow]
                        prev.left = Node(input, canvas, prev)
                        self.animate(canvas, output)

                        # self.explain("{0} inserted".format(input))

                        sr = list(map(int,output.cget('scrollregion').split()))
                        if x<=sr[0]:
                            output.move(tk.ALL,50,0)
                            output.update()
                            output['scrollregion'] = (sr[0],sr[1],sr[2]+100,sr[3])
                        sr = list(map(int, output.cget('scrollregion').split()))

                        if y + 100>= sr[3]:
                            output['scrollregion'] = (sr[0], sr[1], sr[2], sr[3] + 100)
                            output.update()
                    else:
                        ancestor = prev.parent
                        if ancestor and ancestor.val <= prev.val:
                            self.move_all_cnodes(prev, 40, output)
                            output.update()
                else:
                    prev = temp
                    self.animate(prev.canvas, output)
                    ancestor = prev.parent
                    temp = temp.right
                    if not temp:
                        if ancestor and ancestor.val > prev.val:
                            self.move_all_cnodes(prev, -40, output)
                        x, y, x1, y1 = output.coords(prev.canvas[0])
                        arrow = output.create_line(x1, y + 20, x1 + 20, y + 40, arrow=tk.LAST, capstyle=tk.BUTT,
                                                   fill="black")
                        x += 40
                        y += 40

                        curr_circle = output.create_oval(x, y, x + 40, y + 40, fill="black")
                        curr_text = output.create_text(x + 20, y + 20, text=input, fill="white")
                        canvas = [curr_circle, curr_text, arrow]
                        prev.right = Node(input, canvas, prev)
                        self.animate(canvas, output)
                        sr = list(map(int, output.cget('scrollregion').split()))
                        if x >= sr[2]*0.75:
                            output.update()
                            output['scrollregion'] = (sr[0], sr[1], sr[2] + 100, sr[3])
                        sr = list(map(int, output.cget('scrollregion').split()))

                        if y +100 >= sr[3]:
                            output['scrollregion'] = (sr[0], sr[1], sr[2], sr[3] + 100)
                            output.update()
                    else:
                        if ancestor and ancestor.val > prev.val:
                            self.move_all_cnodes(prev, -40, output)
                            sr = list(map(int, output.cget('scrollregion').split()))
                            output.move(tk.ALL, 50, 0)
                            output['scrollregion'] = (sr[0], sr[1], sr[2] + 100, sr[3])
                            output.update()

        # Right sub tree from root
        else:
            while temp:
                if input>=temp.val:

                    prev = temp
                    self.animate(prev.canvas, output)
                    temp = temp.right
                    if not temp:
                        ancestor = prev.parent

                        if ancestor and ancestor.val > prev.val:
                            self.move_all_cnodes(prev, -40, output)
                        x, y, x1, y1 = output.coords(prev.canvas[0])
                        arrow = output.create_line(x1, y + 20, x1 + 20, y + 40, arrow=tk.LAST, capstyle=tk.BUTT,
                                                   fill="black")
                        x += 40
                        y += 40
                        curr_circle = output.create_oval(x, y, x + 40, y + 40, fill="black")
                        curr_text = output.create_text(x + 20, y + 20, text=input, fill="white")
                        canvas = [curr_circle, curr_text, arrow]
                        prev.right = Node(input, canvas, prev)
                        self.animate(canvas, output)
                        sr = list(map(int, output.cget('scrollregion').split()))
                        if x >= sr[2]*0.75:
                            output['scrollregion'] = (sr[0], sr[1], sr[2]+100, sr[3])
                            output.update()
                        sr = list(map(int, output.cget('scrollregion').split()))

                        if y + 100 >= sr[3]:
                            output['scrollregion'] = (sr[0], sr[1], sr[2], sr[3] + 100)
                            output.update()
                    else:
                        ancestor = prev.parent
                        if ancestor and ancestor.val > prev.val:
                            self.move_all_cnodes(prev, -40, output)
                            sr = list(map(int, output.cget('scrollregion').split()))
                            output.move(tk.ALL, 50, 0)
                            output['scrollregion'] = (sr[0], sr[1], sr[2] + 100, sr[3])
                            output.update()
                else:
                    prev = temp
                    self.animate(prev.canvas, output)
                    ancestor = prev.parent
                    temp = temp.left

                    if not temp:
                        if ancestor and ancestor.val <= prev.val:
                            self.move_all_cnodes(prev, 40, output)
                        x, y, x1, y1 = output.coords(prev.canvas[0])
                        arrow = output.create_line(x, y + 20, x - 20, y + 40, arrow=tk.LAST, capstyle=tk.BUTT,
                                                   fill="black")
                        x -= 40
                        y += 40

                        curr_circle = output.create_oval(x, y, x + 40, y + 40, fill="black")
                        curr_text = output.create_text(x + 20, y + 20, text=input, fill="white")
                        canvas = [curr_circle, curr_text, arrow]
                        prev.left = Node(input, canvas, prev)
                        self.animate(canvas,output)
                        sr = list(map(int, output.cget('scrollregion').split()))
                        if x < sr[0]:
                            output.move(tk.ALL,50,0)
                            output['scrollregion'] = (sr[0], sr[1], sr[2] + 100, sr[3])
                            output.update()
                        sr = list(map(int, output.cget('scrollregion').split()))

                        if y + 100 >= sr[3]:
                            output['scrollregion'] = (sr[0], sr[1], sr[2], sr[3] + 100)
                            output.update()
                    else:
                        if ancestor and ancestor.val <= prev.val:
                            self.move_all_cnodes(prev, 40, output)


#search for element
    def search(self, output):
        # input = int(self.node.get())
        # if input == "" or input == "Enter node value":
        #     msg.showwarning(title="No Input", message="Please enter input")
        #     return
        input = self.node.get()
        if input == "" or input == "Enter node value":
            msg.showwarning(title="No Input", message="Please enter input")
            return
        input=int(input)  
        temp = self.root
        while temp:
            if input<temp.val:
                self.animate(temp.canvas,output)
                #msg.showinfo(title="Node found", message="{0} is less than {1}  Hence traversing to left sub tree of {1}".format(input,temp.val))
                temp = temp.left

            elif input>temp.val:
                self.animate(temp.canvas, output)
                #msg.showinfo(title="Node found", message="{0} is greater than or equal to {1}  Hence traversing to right sub tree of {1}".format(input,temp.val))
                temp = temp.right
            
            else:
                self.animate(temp.canvas, output,'#fb5581')
                msg.showinfo(title="Node found", message=" Node {0} found".format(input))
                return
        else:
            # self.explain("{0} is not present in tree".format(input))
            msg.showwarning(title="Not Found",message="{} is not present in tree.".format(input))
            return



    def read(self):
        f1=open("result.txt","r")
        last_line=f1.readlines()[-1]
        print(last_line)
        # self.output.create_text(600,700,fill="darkblue",font="Times 20 italic bold",text=f"Traversal Result: {last_line}\n")
        self.output.create_text(600,700,fill="darkblue",font="Times 20 italic bold",text=f"Traversal Result: {last_line}\n",tags='trav')
        f1.close()
        # time.sleep(10)
       
    def clearFunc(self):
        self.output.delete('trav')
#Traversals - Inorder, Preorder and Postorder
    
    def inorderTraversal(self, temp, output):
        res=[]
        if temp:
            self.animate(temp.canvas, output,'#2acaea')
            res=self.inorderTraversal(temp.left,output)
            res.append(temp.val)
            res=res+self.inorderTraversal(temp.right,output)
            f=open("result.txt","w")
            print(res,file=f)
            f.close()
            
        # print("io",res)
        
        # self.output.create_text(600,700,fill="darkblue",font="Times 20 italic bold",text=f"{res}\n")
        return res

    def preorderTraversal(self, temp, output):
        res=[]
        if temp:
            self.animate(temp.canvas, output,'#c9a0dc')
            res.append(temp.val)
            
            res=res+self.preorderTraversal(temp.left,output)
            res=res+self.preorderTraversal(temp.right,output)
            f=open("result.txt","w")
            print(res,file=f)
            f.close()
        # self.output.create_text(600,700,fill="darkblue",font="Times 20 italic bold",text=f"{RES}\n")
        return res
    
    def postorderTraversal(self, temp, output):
        res=[]
        if temp:
            self.animate(temp.canvas, output,'#ff9100')
            res=self.postorderTraversal(temp.left,output)
            res=res+self.postorderTraversal(temp.right,output)
            res.append(temp.val)
            f=open("result.txt","w")
            print(res,file=f)
            f.close()
        # print("po",res)
        # self.output.create_text(600,700,fill="darkblue",font="Times 20 italic bold",text=f"{res}\n")
        return res 

    def delete(self, output,diffinput=""):
        input = int(self.node.get())
        if diffinput!="":
            input = diffinput[0].val
            temp = diffinput[1]
            prev = temp.parent
            #prev = diffinput[0].parent
            deletion_to_be_made = diffinput[2]
            if prev.parent and temp.val < self.root.val and temp.val<prev.val and prev.parent.val>prev.val:
              deletion_to_be_made.append([prev, 40, output])
            elif prev.parent and temp.val < self.root.val and temp.val > prev.val and prev.parent.val > prev.val:
                deletion_to_be_made.append([prev, 40, output])
            elif prev.parent and temp.val > self.root.val and temp.val>prev.val and prev.parent.val<prev.val:
              deletion_to_be_made.append([prev, -40, output])
            elif prev.parent and temp.val > self.root.val and temp.val < prev.val and prev.parent.val < prev.val:
                deletion_to_be_made.append([prev, -40, output])
            #if temp.val < self.root.val and temp.val<prev.val and prev.parent.val>prev.val:
                #deletion_to_be_made.append([prev, 40, output])
            #elif temp.val > self.root.val and temp.val>prev.val and prev.parent.val<prev.val:
                #deletion_to_be_made.append([prev, -40, output])
        else:
            deletion_to_be_made = []
            if self.root:
                temp = self.root
                prev = self.root
            else:
                msg.showwarning(title="Not Present", message="Root does not exists")
                return

        if input == "" or input == "Enter node value":
            msg.showwarning(title="No Input", message="Please enter input")
            return

        if input == temp.val and diffinput=="":
            self.found_delete(prev, 'root', '', temp, deletion_to_be_made, output)
            return
        elif input == temp.val and diffinput != "":
            self.found_delete(prev, 'not_root', '', temp, deletion_to_be_made, output)
            return

        if input<temp.val:
            while temp:
                if input<temp.val:
                    prev = temp
                    self.animate(prev.canvas,output)
                    temp = temp.left

                    if not temp:
                        msg.showwarning(title="Not Present", message="{} is not present in tree.".format(input))
                        return
                    else:
                        ancestor = prev.parent
                        if ancestor and ancestor.val <= prev.val:
                            deletion_to_be_made.append([prev, -40, output])
                        if input == temp.val:
                            self.animate(temp.canvas, output, '#fb5581')
                            #if diffinput != "" :
                                #diffinput[0].val, diffinput[1].val = diffinput[1].val, diffinput[0].val
                            self.found_delete(prev, 'l', 'l', temp, deletion_to_be_made, output)
                            return

                else:
                    prev = temp
                    self.animate(prev.canvas, output)
                    ancestor = prev.parent
                    temp = temp.right
                    if not temp:
                        msg.showwarning(title="Not Present", message="{} is not present in tree.".format(input))
                        return
                    else:
                        if ancestor and ancestor.val > prev.val:
                            deletion_to_be_made.append([prev, 40, output])
                        if input == temp.val:
                            self.animate(temp.canvas, output, '#fb5581')
                            #if diffinput != "" :
                                #diffinput[0].val, diffinput[1].val = diffinput[1].val, diffinput[0].val
                            self.found_delete(prev, 'l', 'r', temp, deletion_to_be_made, output)
                            return
        else:
            while temp:
                if input>=temp.val:
                    prev = temp
                    self.animate(prev.canvas, output)
                    temp = temp.right
                    if not temp:
                        msg.showwarning(title="Not Present", message="{} is not present in tree.".format(input))
                        return
                    else:
                        ancestor = prev.parent
                        if ancestor and ancestor.val > prev.val:
                            deletion_to_be_made.append([prev, 40, output])
                        if input == temp.val:
                            self.animate(temp.canvas, output, '#fb5581')
                            #if diffinput != "" :
                                #diffinput[0].val, diffinput[1].val = diffinput[1].val, diffinput[0].val
                            self.found_delete(prev, 'r', 'r', temp, deletion_to_be_made, output)
                            return
                else:
                    prev = temp
                    self.animate(prev.canvas, output)
                    ancestor = prev.parent
                    temp = temp.left

                    if not temp:
                        msg.showwarning(title="Not Present", message="{} is not present in tree.".format(input))
                        return
                    else:
                        if ancestor and ancestor.val <= prev.val:
                            deletion_to_be_made.append([prev, -40, output])

                        if input == temp.val:
                            self.animate(temp.canvas, output, '#fb5581')
                            #if diffinput != "" :
                                #diffinput[0].val, diffinput[1].val = diffinput[1].val, diffinput[0].val
                            self.found_delete(prev, 'r', 'l', temp, deletion_to_be_made, output)
                            return

    def deletetext(self,event):
        event.widget.delete(0,"end")
        return None

    def found_delete(self,prev,dir1,dir2,temp,deletion_to_be_made,output):
        if temp.left is None and temp.right is None:
            if dir1=="not_root":
                if prev.val>=temp.val:
                    prev.right = None
                else:
                    prev.left = None
            elif dir1 == "root":
                self.root = None
            if dir2 == "l":
                prev.left = None
            elif dir2 == "r":
                prev.right = None
            canvas = temp.canvas
            output.delete(canvas[0], canvas[1], canvas[2])
            for i in range(len(deletion_to_be_made)):
                self.move_all_cnodes(deletion_to_be_made[i][0], deletion_to_be_made[i][1], deletion_to_be_made[i][2],
                                     True)
            return
        elif temp.left and (temp.right is None):
            if dir1 == "not_root":
                canvas = temp.canvas
                output.delete(canvas[0], canvas[1], canvas[2])
                prev.left = temp.left
                temp.left.parent = prev
                for i in range(len(deletion_to_be_made)):
                    self.move_all_cnodes(deletion_to_be_made[i][0], deletion_to_be_made[i][1],
                                         deletion_to_be_made[i][2],
                                         True)
                self.move_all_cnodes(temp.left, 40, output, True, -40)

            elif dir1 == "root":
                canvas = temp.canvas
                output.delete(canvas[0], canvas[1], canvas[2])
                output.delete(temp.left.canvas[2])

                temp.left.parent = None
                self.root = temp.left
                output.move(tk.ALL,40,-40)
            else:
                if prev.val<=temp.val:
                    prev.right = temp.left
                    temp.left.parent = prev
                    canvas = temp.canvas
                    output.delete(canvas[0], canvas[1], canvas[2])
                    for i in range(len(deletion_to_be_made)):
                        self.move_all_cnodes(deletion_to_be_made[i][0], deletion_to_be_made[i][1],
                                             deletion_to_be_made[i][2],
                                             True)

                    self.move_all_cnodes(temp.left, 0, output, True, -40)
                else:

                    prev.left = temp.left
                    temp.left.parent = prev
                    canvas = temp.canvas
                    output.delete(canvas[0], canvas[1], canvas[2])
                    for i in range(len(deletion_to_be_made)):
                        self.move_all_cnodes(deletion_to_be_made[i][0], deletion_to_be_made[i][1],
                                             deletion_to_be_made[i][2],
                                             True)

                    self.move_all_cnodes(temp.left,40,output,True,-40)

            return
        elif temp.right and (temp.left is None):
            if dir1 == "not_root":
                canvas = temp.canvas
                output.delete(canvas[0], canvas[1], canvas[2])
                prev.right = temp.right
                temp.right.parent = prev
                for i in range(len(deletion_to_be_made)):
                    self.move_all_cnodes(deletion_to_be_made[i][0], deletion_to_be_made[i][1],
                                         deletion_to_be_made[i][2],
                                         True)
                self.move_all_cnodes(temp.right, -40, output, True, -40)

            elif dir1 == "root":
                canvas = temp.canvas
                output.delete(canvas[0], canvas[1], canvas[2])
                output.delete(temp.right.canvas[2])

                temp.right.parent = None
                self.root = temp.right
                output.move(tk.ALL,-40,-40)

            else:
                if prev.val>temp.val:
                    prev.left = temp.right
                    temp.right.parent = prev
                    canvas = temp.canvas
                    output.delete(canvas[0], canvas[1], canvas[2])

                    for i in range(len(deletion_to_be_made)):
                        self.move_all_cnodes(deletion_to_be_made[i][0], deletion_to_be_made[i][1],
                                             deletion_to_be_made[i][2],
                                             True)
                    self.move_all_cnodes(temp.right, 0, output, False, -40)
                else:
                    prev.right = temp.right
                    temp.right.parent = prev
                    canvas = temp.canvas
                    output.delete(canvas[0], canvas[1], canvas[2])

                    for i in range(len(deletion_to_be_made)):
                        self.move_all_cnodes(deletion_to_be_made[i][0], deletion_to_be_made[i][1],
                                             deletion_to_be_made[i][2],
                                             True)
                    self.move_all_cnodes(temp.right, -40, output, True, -40)
            return
        else:
            temp_n = temp.right
            prev_n = temp_n
            while temp_n:
                    prev_n = temp_n
                    temp_n = temp_n.left
            output.itemconfig(temp.canvas[1], text=prev_n.val)
            output.itemconfig(prev_n.canvas[1], text=temp.val)
            output.update()
            time.sleep(1)
            temp.val,prev_n.val = prev_n.val,temp.val
            self.delete(output, [prev_n, temp.right, deletion_to_be_made])
            return

    def move_all_cnodes(self,parent,byx,output,rev=False,byy=0):
        q = [parent]
        ancestor = parent.parent
        xa,ya,xa1,ya1 = output.coords(ancestor.canvas[0])
        if rev:
            xa,xa1 = xa1,xa


        while len(q):
            prev = q[0]
            output.move(prev.canvas[0],byx,byy)
            output.move(prev.canvas[1], byx, byy)
            output.move(prev.canvas[2], byx, byy)

            output.update()
            if prev.left:
                q.append(prev.left)
            if prev.right:
                q.append(prev.right)
            q.pop(0)
        xp, yp, xp1, yp1 = output.coords(parent.canvas[0])
        if byx>0:
            output.coords(parent.canvas[2], xa1, ya + 20, xp+20,yp)
        else:
            output.coords(parent.canvas[2], xa, ya + 20, xp + 20, yp)

    def animate(self,node,output,color='#3be13b'):
        output.itemconfig(node[0], fill=color)
        output.itemconfig(node[1], fill="black")
        output.update()
        time.sleep(0.3)
        output.itemconfig(node[0], fill="black")
        output.itemconfig(node[1], fill="white")
        output.update()

    
