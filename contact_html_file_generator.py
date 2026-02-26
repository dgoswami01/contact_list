# input_file = r"FILE_PATH"
# output_file = r"FILE_PATH"

input_file = r"C:\Users\KIIT\Downloads\dropdown (1).txt"
output_file = r"C:\Users\KIIT\Desktop\PROGRAMMING\Python\file_formatting\contacts_final.html"


# with open(input_file, "r", encoding="utf-8") as infile, \
#      open(output_file, "w", encoding="utf-8") as outfile:

#     outfile.write("<html><body>\n")
#     outfile.write("<h2>Contact List</h2>\n")

#     for line in infile:
#         line = line.strip()
#         if not line:
#             continue
        
#         try:
#             name = line.split("[")[0].strip()
#             number = line.split("Contact:")[1].split("]")[0].strip().replace(".", "")

#             outfile.write(f'<p><a href="tel:{number}">{name} - {number}</a></p>\n')
        
#         except IndexError:
#             print("Skipping invalid line:", line)

#     outfile.write("</body></html>")

# print("Clickable contact HTML file created!")



country_code = "91"  # Change if needed

contacts = []

# --------- Read and Extract Contacts ---------
with open(input_file, "r", encoding="utf-8") as infile:
    for line in infile:
        line = line.strip()
        if not line:
            continue
        
        try:
            name = line.split("[")[0].strip()
            number = line.split("Contact:")[1].split("]")[0].strip().replace(".", "")
            contacts.append((name, number))
        except IndexError:
            print("Skipping invalid line:", line)

# --------- Sort Alphabetically ---------
contacts.sort(key=lambda x: x[0].lower())

# --------- Generate HTML ---------
with open(output_file, "w", encoding="utf-8") as outfile:
    outfile.write("""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Contact List</title>

<style>
body {
    font-family: Arial, sans-serif;
    padding: 20px;
    background-color: #f5f5f5;
}
h2 {
    text-align: center;
}
.contact {
    display: flex;
    align-items: flex-start;
    background: white;
    position: relative;
    padding: 15px;
    margin-bottom: 10px;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}
.contact.checked {
    background-color: #e6ffe6;
}
.numbering {
    font-weight: bold;
    width: 35px;
}
.details {
    flex-grow: 1;
}
a {
    text-decoration: none;
    margin-right: 15px;
    font-weight: bold;
}
.search-box {
    width: 100%;
    padding: 8px;
    margin-bottom: 15px;
    font-size: 16px;
}
</style>

<script>

const STORAGE_PREFIX = "MaaKamakhyaDevalay_2026_contact_tracker_state_checked_";

function toggleCheck(checkbox, number) {
    const key = STORAGE_PREFIX + number;

    if (checkbox.checked) {
        localStorage.setItem(key, "true");
        checkbox.closest(".contact").classList.add("checked");
    } else {
        localStorage.removeItem(key);
        checkbox.closest(".contact").classList.remove("checked");
    }
}

function loadChecks() {
    document.querySelectorAll("input[type='checkbox']").forEach(cb => {
        const key = STORAGE_PREFIX + cb.value;

        if (localStorage.getItem(key)) {
            cb.checked = true;
            cb.closest(".contact").classList.add("checked");
        }
    });
}

function searchContacts() {
    let input = document.getElementById("search").value.toLowerCase();

    document.querySelectorAll(".contact").forEach(contact => {
        let text = contact.innerText.toLowerCase();
        contact.style.display = text.includes(input) ? "flex" : "none";
    });
}

function resetChecks() {
    Object.keys(localStorage).forEach(function(key) {
        if (key.startsWith(STORAGE_PREFIX)) {
            localStorage.removeItem(key);
        }
    });
    location.reload();
}

window.onload = loadChecks;

</script>

</head>
<body>

<button onclick="resetChecks()" 
        style="
            position: absolute;
            top: 15px;
            right: 20px;
            padding: 8px 14px;
            background-color: #d9534f;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 14px;
            z-index: 1000;
        ">
    Reset All Checks
</button>

<h2>Maa Kamakhya Devalay Panda Contact List</h2>

<input type="text" id="search" class="search-box" 
placeholder="Search contact..." onkeyup="searchContacts()">
""")

#     # Add row number using enumerate
#     for index, (name, number) in enumerate(contacts, start=1):
#         whatsapp_number = country_code + number

#         outfile.write(f"""
# <div class="contact">
#     <div class="numbering">{index}.</div>

#     <div class="details">
#         <input type="checkbox" value="{number}" 
#             onchange="toggleCheck(this, '{number}')">
#         <strong>{name}</strong><br><br>
#         <a href="tel:{number}">📞 {number} </a>
#         <a href="https://wa.me/{whatsapp_number}" target="_blank">💬 WhatsApp</a>
#     </div>
# </div>
# """)

    # Add row number using enumerate
    for index, (name, number) in enumerate(contacts, start=1):
        whatsapp_number = country_code + number

        outfile.write(f"""
    <div class="contact">
        <div class="numbering">{index}.</div>

        <div class="details">
            <strong>{name}</strong><br><br>

            <a href="tel:{number}">📞 {number}</a>
            &nbsp;&nbsp;
            <a href="https://wa.me/{whatsapp_number}" target="_blank">💬 WhatsApp</a>
        </div>

        <input type="checkbox"
            value="{number}"
            onchange="toggleCheck(this, '{number}')"
            style="
                position:absolute;
                top:10px;
                right:10px;
                transform: scale(1.2);
                cursor:pointer;
            ">
    </div>
    """)

    outfile.write("""
</body>
</html>
""")

print("✅ Smart Contact HTML file with numbering created successfully!")
