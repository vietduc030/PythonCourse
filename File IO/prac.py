with open("text.txt","w") as file:
    file.write("Mein Name ist Duc. Mir macht programmieren sehr Spass.\nIch habe festgestellt, dass CHAT GPT ein sehr guter Lehrer ist.\n Er bringt mir Sachen blitzschnell bei.\n Ich nehme es auf wie ein Schwamm.")


with open("text.txt","a") as file:
    file.write("\nIch habe dieses Konzept und die Syntax in 10minuten gelernt.")

with open("text.txt","r") as file:
    file_content=file.read()

print(file_content)