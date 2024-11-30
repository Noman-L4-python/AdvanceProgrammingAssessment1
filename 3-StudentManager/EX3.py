import tkinter as tk
from tkinter import messagebox

def loadData(file_path):
    students = []
    try:
        with open(file_path, "r") as file:
            studentCount = file.readline().strip()
            if not studentCount.isdigit():
                messagebox.showerror("Error", "The first line should be the number of students.")
                return []

            for line in file:
                details = line.strip().split(",")
                if len(details) != 6:
                    messagebox.showerror("Error", "Each student record must contain 6 fields.")
                    return []

                studentId = int(details[0])
                name = details[1].strip()
                coursework = sum(map(int, details[2:5]))
                examMark = int(details[5])
                totalScore = coursework + examMark
                percentage = (totalScore / 160) * 100
                grade = "A" if percentage >= 70 else "B" if percentage >= 60 else "C" if percentage >= 50 else "D" if percentage >= 40 else "F"
                students.append({"id": studentId, "name": name, "coursework": coursework, "exam": examMark, "total": totalScore, "percentage": percentage, "grade": grade})
    except:
        messagebox.showerror("Error", "There was an error reading the student data file.")
    return students

def displayAll():
    if not studentRecords:
        messagebox.showinfo("Information", "No student data available.")
        return
    output = ""
    for student in studentRecords:
        output += f"{student['name']} (ID: {student['id']}): Coursework: {student['coursework']}, Exam: {student['exam']}, Percentage: {student['percentage']:.2f}%, Grade: {student['grade']}\n"
    output += f"\nTotal Students: {len(studentRecords)}, Average Percentage: {sum(s['percentage'] for s in studentRecords) / len(studentRecords):.2f}%"
    resultLabel.config(text=output)

def displayIndividual():
    studentSearch = searchEntry.get().strip().lower()
    for student in studentRecords:
        if student["name"].lower() == studentSearch:
            resultLabel.config(text=f"{student['name']} (ID: {student['id']}): Coursework: {student['coursework']}, Exam: {student['exam']}, Percentage: {student['percentage']:.2f}%, Grade: {student['grade']}")
            return
    messagebox.showinfo("Information", "Student not found.")

def displayHighest():
    if not studentRecords:
        messagebox.showinfo("Information", "No data available.")
        return
    highestScorer = max(studentRecords, key=lambda s: s["total"])
    resultLabel.config(text=f"Highest Scorer: {highestScorer['name']} (ID: {highestScorer['id']}): Coursework: {highestScorer['coursework']}, Exam: {highestScorer['exam']}, Percentage: {highestScorer['percentage']:.2f}%, Grade: {highestScorer['grade']}")

def displayLowest():
    if not studentRecords:
        messagebox.showinfo("Information", "No data available.")
        return
    lowestScorer = min(studentRecords, key=lambda s: s["total"])
    resultLabel.config(text=f"Lowest Scorer: {lowestScorer['name']} (ID: {lowestScorer['id']}): Coursework: {lowestScorer['coursework']}, Exam: {lowestScorer['exam']}, Percentage: {lowestScorer['percentage']:.2f}%, Grade: {lowestScorer['grade']}")

root = tk.Tk()
root.title("Student Record System")
root.geometry("600x400")

studentRecords = loadData("studentMarks.txt")

searchEntry = tk.Entry(root)
searchEntry.pack(pady=10)

tk.Button(root, text="Show All Records", command=displayAll).pack(pady=5)
tk.Button(root, text="Search Individual Record", command=displayIndividual).pack(pady=5)
tk.Button(root, text="Show Highest Scorer", command=displayHighest).pack(pady=5)
tk.Button(root, text="Show Lowest Scorer", command=displayLowest).pack(pady=5)

resultLabel = tk.Label(root, text="", wraplength=500, justify="left")
resultLabel.pack(pady=10)

root.mainloop()
