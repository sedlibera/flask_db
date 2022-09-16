from app import db, Message

# READ
# all_messages = Message.query.all()
# print(all_messages)
#
# message_1 = Message.query.get(1)
# print(message_1)  # repr rezultatas
# print(message_1.message)  # per objekto atributą
#
# message_antanas = Message.query.filter_by(name="Antanas").all()
# print(message_antanas)
#
# # UPDATE
# antanas = Message.query.get(2)
# antanas.email = "blogas.antanas@gmail.com"
# db.session.commit()
#
# # DELETE
# jonas = Message.query.get(1)
# db.session.delete(jonas)
# db.session.commit()

print(Message.query.all())