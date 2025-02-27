    refno = self.comboboxref.get()
            cursor = connection.cursor()

            cursor.execute("delete from med_info where reference_number=%s",(refno,))
            connection.commit()
            connection.close()
            messagebox.showinfo('Deleted',"Data Has Been Deleted")