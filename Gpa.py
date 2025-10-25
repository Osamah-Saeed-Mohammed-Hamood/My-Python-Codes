subjects_weights = {
    #Level one Semster 1
    "Arabic Language 1": 2,
    "Computers Fundmentals": 3,
    "General Physics":3,
    "English Language 1": 2,
    "Islamic Cluture": 2,
    "Calculus 1":2,
    "National Cluture": 2,
    #Level one Semster 2
    "Arabic Language 2": 2,
    "Programming Fundamentals":3,
    "Digital Logic Design":3,
    "English Language 2": 2,
    "Calculus 2":2,
    "Information Technology Fund":3,
    "Skills of Comm & Creative Thinking":2,
    "Arab Israil Confilict":2,
    #Level Two Semster 1
    "Structure Programming": 3,
    "Discrete Structures": 2,
    "Introduction to DataBase":3,
    "Accounting Principles": 2,
    "Differentioal Equations": 2,
    "Advanced Information Tech":2,
    "Linear Algebra": 2,
    #Level Two Semster 2
    "Object Oriented Programming": 3,
    "Data Structure":3,
    "DataBase Systems Design":3,
    "Probability & Statistics": 2,
    "Research Methodlogy":2,
    "Computers Architechture":3,
    #Level Three Semster 1
    "Visual Programming": 3,
    "Computer Network": 3,
    "Algorithms":3,
    "Artificial Intelligence": 3,
    "Applied Numerical Analysis": 3,
    "Opreating Systems":3,
    "Web Design": 3,
    #Level Three Semster 2
    "Web Devlopment": 3,
    "Computaional Theory":2,
    "Advanced Programming":3,
    "Data Mining":3,
    "Computer Graphics":3,
    "Systems Analysis & Design":3,
    #Level Three Semster 1
    "Software Engineering": 3,
    "Client-Server Programming": 3,
    "Compilers Construction":3,
    "Cryptography": 3,
    "Digital Image Processing": 3,
    #Level Three Semster 2
    "Network Design And Mangment": 3,
    "Cloud Computing":3,
    "IT Project Mangment":2,
    "AI Applications":3,
}

weighted_scores = []

for subject, weight in subjects_weights.items():
    score = float(input(f"Enter your score in {subject}: "))
    weighted_scores.append(score * weight)
print(f"All Subject After Weight:{weighted_scores}")
total_weighted_score = sum(weighted_scores)
gpa = total_weighted_score / 131

# Output the GPA to the user
print(f"Your GPA is: {gpa:.2f}")
print(f"Your Total is: {total_weighted_score}")