import customtkinter

main = customtkinter.CTk()

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
main.title("bruh")

main.geometry("1920*1080")

Butt_On = customtkinter.CTkButton(main,40,28,fg_color="transparent")
Butt_On.pack(pady = 100)
frame1 = customtkinter.CTkScrollableFrame(main,width = 150, height = 1080)
frame1.place(x =0, y= 0)

for a in range(200):
    test_button = customtkinter.CTkButton(frame1,text = "bruh",width =80,height = 30,fg_color="transparent",hover_color="grey").pack(pady = 10)

main.mainloop()