from pyscript import document, display

def club1(e):
    club1 = {
        "NAME": "FILM CLUB",
        "ABOUT": "A CREATIVE SPACE FOR STUDENTS TO EXPRESS THEMSELVES THROUGH FILM.",
        "TIME": "FRIDAY, 3PM",
        "LOC.": "ROOM 101, 2ND FLOOR ",
        "MOD.": "MR. ANDERSON",
        "MEMBERS": 35,
    }
    
    document.getElementById("output").innerHTML = ""
    document.getElementById("info").innerHTML = ""
    
    display(f'NAME: ', target="info")
    display(f'ABOUT: ', target="info")
    display(f'TIME: ', target="info")
    display(f'LOCATION: ', target="info")
    display(f'MODERATOR: ', target="info")
    display(f'MEMBERS: ', target="info")
    
    display(f'{club1['NAME']}', target="output")
    display(f'{club1['ABOUT']}', target="output")
    display(f'{club1['TIME']}', target="output")
    display(f'{club1['LOC.']}', target="output")
    display(f'{club1['MOD.']}', target="output")
    display(f'{club1['MEMBERS']}', target="output")
    
def club2(e):
    club2 = {
        "NAME": "MUSIC ENGINEERING CLUB",
        "ABOUT": "A CLUB WHERE STUDENTS CREATE MUSIC THROUGH AUDIO TECHNOLOGY.",
        "TIME": "WEDNESDAY, 2PM",
        "LOC.": "ROOM 103, 2ND FLOOR ",
        "MOD.": "MR. WEST",
        "MEMBERS": 30,
    }
    
    document.getElementById("output").innerHTML = ""
    document.getElementById("info").innerHTML = ""
    
    display(f'NAME: ', target="info")
    display(f'ABOUT: ', target="info")
    display(f'TIME: ', target="info")
    display(f'LOCATION: ', target="info")
    display(f'MODERATOR: ', target="info")
    display(f'MEMBERS: ', target="info")
    
    display(f'{club2['NAME']}', target="output")
    display(f'{club2['ABOUT']}', target="output")
    display(f'{club2['TIME']}', target="output")
    display(f'{club2['LOC.']}', target="output")
    display(f'{club2['MOD.']}', target="output")
    display(f'{club2['MEMBERS']}', target="output")
    
def club3(e):
    club3 = {
        "NAME": "GRAPHIC DESIGNING CLUB",
        "ABOUT": "A CLUB WHERE STUDENTS CREATE VISUAL CONTENT USING DIGITAL TOOLS.",
        "TIME": "MONDAY, 4PM",
        "LOC.": "ROOM 104, 2ND FLOOR ",
        "MOD.": "MR. GARCIA",
        "MEMBERS": 40,
    }
    
    document.getElementById("output").innerHTML = ""
    document.getElementById("info").innerHTML = ""
    
    display(f'NAME: ', target="info")
    display(f'ABOUT: ', target="info")
    display(f'TIME: ', target="info")
    display(f'LOCATION: ', target="info")
    display(f'MODERATOR: ', target="info")
    display(f'MEMBERS: ', target="info")
    
    display(f'{club3['NAME']}', target="output")
    display(f'{club3['ABOUT']}', target="output")
    display(f'{club3['TIME']}', target="output")
    display(f'{club3['LOC.']}', target="output")
    display(f'{club3['MOD.']}', target="output")
    display(f'{club3['MEMBERS']}', target="output")

def calculate(e):
    output_summary = document.getElementById("output2")
    output_summary.innerHTML = ""
    
    firstName = document.getElementById("fName").value
    lastName = document.getElementById("lName").value
    
    subject1 = int(document.getElementById("subject1").value)
    subject2 = int(document.getElementById("subject2").value)
    subject3 = int(document.getElementById("subject3").value)
    subject4 = int(document.getElementById("subject4").value)
    subject5 = int(document.getElementById("subject5").value)
    subject6 = int(document.getElementById("subject6").value)
    
    units = [5, 5, 2, 5, 5, 1] # Units for each subject
    Sci, Eng, ICT_unit, Math, Fil, PE_unit = units # Unpacking units
    
    GWA = ((subject1 * Sci) + (subject2 * Eng) + (subject3 * ICT_unit) + (subject4 * Math) + (subject5 * Fil) + (subject6 * PE_unit))/(Sci + Eng + ICT_unit + Math + Fil + PE_unit)
    
    final_message = f"""Hello, <strong>{firstName} {lastName}</strong><br><br>
    Science: {subject1}<br>
    English: {subject2}<br>
    ICT: {subject3}<br>
    Math: {subject4}<br>
    Filipino: {subject5}<br
    PE: {subject6}<br><br>
    <strong>Your General Weighted Average (GWA) is:</strong> {round(GWA, 2)}
    """
    output_summary.innerHTML = final_message