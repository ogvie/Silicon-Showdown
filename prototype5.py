from tkinter import *
from tkinter import simpledialog
from tkinter import ttk
import customtkinter # Import a custom tkinter module (assumption)
import requests

# Hexadecimal color codes for styling purposes
mycolour = "#383434"   # Dark background or text color
mycolour2 = "#ececec"   # Light color for contrasting elements or backgrounds
mycolour3 = "#FF6961"   # Color associated with red shades
mycolour4 = "#77DD77"   # A shade of green

# Initialize the Tkinter root window
root = Tk()
# root.geometry('2560x1440')
root.geometry('1920x1080')
root.configure(bg=mycolour)
#root.attributes('-fullscreen', True) # Set the initial dimensions of the window
root.title("Silicon Showdown")

# Class for managing the Silicon Showdown game
class SiliconShowdown:
    def __init__(self, root, categories, questions, answers):
        self.root = root
        self.root.title("Silicon Showdown - In Game")

        self.categories = categories # List of categories for the Jeopardy board
        self.prices = ["100", "200", "300", "400", "500"]

        self.score_label = Label(self.root, text="Score: 0", font=("font2.ttf", 25, "bold"))
        self.score_label.grid(row=7, column=0, columnspan=6) # Place the score label in the window

        self.questions = questions # Dictionary containing questions for each category and price
        self.answers = answers # Dictionary containing answers for each category and price

        self.score = 0

        self.create_ui()

    def create_ui(self):
        self.buttons = {} # A dictionary to store references to game buttons

        for col, category in enumerate(self.categories):
            category_label = Label(self.root, text=category, font=("font2.ttf", 20, "bold"))
            category_label.grid(row=0, column=col) # Place the category labels in the window


            for row, price in enumerate(self.prices):
                button = Button(self.root, text=price, font=("font2.ttf", 20, "bold"), width=20, height=4, state=NORMAL)
                button.grid(row=row + 1, column=col) # Place the buttons in the window
                self.buttons[(col, row)] = button # Store the button in a dictionary

                button.config(command=lambda c=category, p=price: self.show_question(c, p))

    def show_question(self, category, price):
        if self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] == NORMAL:
            question = self.questions[category][self.prices.index(price)]
            answer = self.answers[category][self.prices.index(price)]
            player_answer = simpledialog.askstring("Question", f"Category: {category}\nPrice: {price}\n\n{question}\n\nYour Answer:")

            if player_answer and player_answer.lower() == answer.lower():
                self.score += int(price)
                self.update_score()
                self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] = DISABLED
                self.buttons[(self.categories.index(category), self.prices.index(price))]['bg'] = 'mycolour4'
                self.check_game_over()
            else:
                self.score -= int(price)
                self.update_score()
                self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] = DISABLED
                self.buttons[(self.categories.index(category), self.prices.index(price))]['bg'] = 'mycolour3'
                self.check_game_over()

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")

    def check_game_over(self):
        if all(self.buttons[(col, row)]['state'] == DISABLED for col in range(6) for row in range(5)):
            game_over_label = Label(self.root, text="Game Over!", font=("font2.ttf", 25, "bold"), fg="red")
            game_over_label.grid(row=6, column=0, columnspan=6)

def clear():
    for item in root.winfo_children():
        item.destroy()

def main_menu():
    clear()

    root.title("Silicon Showdown - Main Menu")

    # Buttons for the main menu
    playbtn = Button(root, text="Play", command=topicselector, font=("LEMONMILK-Regular.otf", 40), width=10, height=2)
    optionsbtn = Button(root, text="Options", command=options, font=("LEMONMILK-Regular.otf", 40), width=10, height=2)
    aboutbtn = Button(root, text="About", command=about, font=("LEMONMILK-Regular.otf", 40), width=10, height=2)
    exitbtn = Button(root, text='Exit', command=root.destroy, font=("LEMONMILK-Regular.otf", 40), width=10, height=2)
    eastereggbtn = Button(root, text="???", command=easteregg)

    playbtn.pack(side='top', padx=10, pady=10)
    optionsbtn.pack(side='top', padx=10, pady=10)
    aboutbtn.pack(side='top', padx=10, pady=10)
    exitbtn.pack(side='top', padx=10, pady=10)
    eastereggbtn.pack(side='top')

def topicselector():
    clear()

    root.title("Silicon Showdown - Topic Selector")

    # Buttons for selecting different topics
    oneonebtn = Button(root, text="1.1 - Processors and Storage Devices", command=oneone, font=("font2.ttf", 40))
    onetwobtn = Button(root, text="1.2 - Software and software development", command=onetwo, font=("font2.ttf", 40))
    onethreebtn = Button(root, text="1.3 - Exchanging data", command=onethree, font=("font2.ttf", 40))
    onefourbtn = Button(root, text="1.4 - Data types, data structures and algorithms", command=onefour, font=("font2.ttf", 40))
    onefivebtn = Button(root, text="1.5 - Legal, moral, cultural and ethical issues", command=onefive, font=("font2.ttf", 40))
    twoonebtn = Button(root, text="2.1 - Elements of computational thinking", command=twoone, font=("font2.ttf", 40))
    twotwobtn = Button(root, text="2.2 - Problem solving and programming", command=twotwo, font=("font2.ttf", 40))
    twothreebtn = Button(root, text="2.3 - Algorithms", command=twothree, font=("font2.ttf", 40))
    backbtn = Button(root, text="Back", font=("font2.ttf", 20), command=main_menu)
    
    oneonebtn.pack(side='top', padx=10, pady=10)
    onetwobtn.pack(side='top', padx=10, pady=10)
    onethreebtn.pack(side='top', padx=10, pady=10)
    onefourbtn.pack(side='top', padx=10, pady=10)
    onefivebtn.pack(side='top', padx=10, pady=10)
    twoonebtn.pack(side='top', padx=10, pady=10)
    twotwobtn.pack(side='top', padx=10, pady=10)
    twothreebtn.pack(side='top', padx=10, pady=10)
    backbtn.pack(side='top', padx=10, pady=10)

def oneone():
    # Clear the screen or perform any necessary setup
    clear()

    # Define custom quiz categories for the first set of topics
    custom_categories11 = ["Processor Basics", "Processor Types", "Computer Architecture", "I/O Devices", "Storage Devices", "Memory",]

    # Define quiz questions for each category
    questions11 = {
        "Processor Basics": ["Are registers part of the processor?", "What does the F in FDE Cycle stand for?", "The higher the clock speed, the ______ instructions are carried out", "The accumulator ___________ stores data while instructions or calculations are being carried out.", "Pipelining improves __________."],
        "Processor Types": ["What does CISC stand for?", "Between CISC and RISC, which consumes less power?", "GPUs can be used for ________ processing.", "Are parallelism and concurrency the same thing?", "Does double the number of cores mean double the performance?"],
        "Computer Architecture": ["Out of Von Neumann and Harvard architecture, which has a simpler operating system?", "Instructions and data stored in separate memory units in _______ architecture.", "Von Neumann architecture uses the same _______ bus and data bus.", "Reading and writing data can be done at the same time as fetching an instruction in which architecture?", "Does contemporary processing use only Von Neumann architecture?"],
        "I/O Devices": ["Are speakers an input or output device?", "Can a device be both input and output?", "Is a microphone an input or output device?", "Is a monitor an input or output device?", "Is a touch screen an input or output device?"],
        "Storage Devices": ["What does SSD stand for?", "Can you write data to a DVD?", "A hard drive stores data using ________ storage.", "What kind of storage are CDs?", "Which type of storage has moving parts?"],
        "Memory": ["Which memory is non-volatile?", "Which is primary memory?", "What does ROM stand for?", "Virtual memory is used when ___ is full.", "Is cache memory faster than RAM?"]
    }

    # Define answers for each category
    answers11 = {
        "Processor Basics": ["Yes", "Fetch", "faster", "temporarily", "efficiency"],
        "Processor Types": ["Complex instruction set computer", "RISC", "parallel", "No", "No"],
        "Computer Architecture": ["Von Neumann", "harvard", "address", "Harvard", "No"],
        "I/O Devices": ["Output", "Yes", "Input", "Output", "Both"],
        "Storage Devices": ["Solid State Drive", "Yes", "magnetic", "Optical", "Magnetic"],
        "Memory": ["ROM", "RAM", "Read Only Memory", "RAM", "Yes"]
    }

    # Configure the layout of the GUI
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.columnconfigure(3, weight=1)
    root.columnconfigure(4, weight=1)
    root.columnconfigure(5, weight=1)

    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)
    root.rowconfigure(4, weight=1)
    root.rowconfigure(5, weight=1)
    root.rowconfigure(6, weight=1)
    root.rowconfigure(7, weight=1)
    root.rowconfigure(8, weight=1)

    # Create a "Back" button to return to the topic selection screen
    backbtn = Button(root, text="Back", font=("font2.ttf", 20), command=topicselector)
    backbtn.grid(row=8, column=0, columnspan=6)

    # Initialize the quiz for the given topics
    SiliconShowdown(root, custom_categories11, questions11, answers11)

def onetwo():
    # Clear the screen or perform any necessary setup
    clear()

    # Define custom quiz categories for the first set of topics
    custom_categories12 = ["Systems Software", "Applications Generation", "Software Development", "Types of Programming Language", "Types of Software and Methodologies", "Programming Language Characteristics"]

    # Define quiz questions for each category
    questions12 = {
    "Systems Software": ["Why is an operating system necessary for a computer?", "What is the function of memory management in an operating system?", "Explain the role of interrupts in computing.", "What are the different scheduling algorithms, and how do they prioritize tasks?", "Differentiate between distributed and Real-Time operating systems."],
    "Applications Generation": ["Define utilities in the context of software applications.", "What is the significance of open source versus closed source software?", "Distinguish between interpreters and compilers.", "Describe the stages of compilation in software development.", "Explain the role of linkers and loaders in a compiled program."],
    "Software Development": ["What are the key principles of the waterfall lifecycle in software development?", "Name two agile methodologies in software development.", "What is the main idea behind extreme programming (XP)?", "Discuss the merits and drawbacks of the spiral model in software development.", "When might rapid application development (RAD) be a suitable choice in software development?"],
    "Types of Programming Language": ["Why do different programming paradigms exist, and what purpose do they serve?", "Give an example of a procedural programming language.", "Explain the concept of assembly language and its use.", "What are the modes of addressing memory, and how do they differ?", "Define key concepts in object-oriented languages, such as inheritance and encapsulation."],
    "Types of Software and Methodologies": ["What is the role of BIOS in a computer system?", "Explain the function of device drivers in the context of software.", "How does virtual memory contribute to efficient system operation?", "Define the characteristics of multi-tasking operating systems.", "What distinguishes Real-Time operating systems from other types of operating systems?"],
    "Programming Language Characteristics": ["Why is there a need for various programming paradigms?", "Give an example of an object-oriented language and explain its key concepts.", "Describe the Little Man Computer instruction set in assembly language.", "In what scenarios would using an assembly language be advantageous?", "Discuss the characteristics of open-source and closed-source software."]
    }

    # Define answers for each category
    answers12 = {
    "Systems Software": [ "An operating system manages hardware resources and provides services for computer programs.", "Memory management handles data storage, retrieval, and allocation in the computer's memory.", "Interrupts are signals that halt the normal execution of a program, allowing the processor to handle external events.", "Scheduling algorithms include round robin, first come first served, multi-level feedback queues, shortest job first, and shortest remaining time.", "Distributed operating systems manage tasks across multiple computers, while Real-Time operating systems prioritize quick response to external events."],
    "Applications Generation": ["Utilities are software tools that perform specific tasks, such as file management or system maintenance.", "Open source software allows users to view and modify the source code, while closed source keeps the code proprietary.", "Interpreters execute code line by line, while compilers translate the entire code into machine language before execution.", "Compilation involves lexical analysis, syntax analysis, code generation, and optimization.", "Linkers combine program modules, while loaders load the compiled program into memory for execution."],
    "Software Development": ["The waterfall model follows a linear, sequential approach with distinct phases like requirements, design, implementation, testing, deployment, and maintenance.", "Scrum and Kanban are examples of agile methodologies.", "Extreme programming emphasizes frequent releases, continuous testing, and collaboration between developers and customers.", "The spiral model allows for iterative development but may result in increased complexity.", "RAD is suitable for projects with well-defined requirements and a need for quick delivery."],
    "Types of Programming Language": ["Programming paradigms provide a set of principles for structuring and designing code to solve specific types of problems.", "C is an example of a procedural programming language.", "Assembly language is a low-level programming language using mnemonic codes and is closely tied to machine code.", "Modes include immediate, direct, indirect, and indexed addressing, each specifying how the operand is located.", "Inheritance allows a class to inherit properties from another, and encapsulation involves bundling data and methods into a single unit."],
    "Types of Software and Methodologies": ["BIOS initializes hardware components and facilitates the booting of the operating system.", "Device drivers enable communication between the operating system and specific hardware devices.", "Virtual memory allows the operating system to use disk space as an extension of RAM, enhancing the system's capabilities.", "Multi-tasking OS allows multiple tasks to run concurrently, improving overall system efficiency.", "Real-Time operating systems prioritize immediate response to external events, critical in time-sensitive applications."],
    "Programming Language Characteristics": ["Different paradigms provide diverse approaches to problem-solving, catering to different programming needs.", "Java is an object-oriented language with features like classes, objects, methods, attributes, inheritance, encapsulation, and polymorphism.", "The Little Man Computer instruction set includes basic operations like ADD, SUB, STORE, LOAD, etc., simulating a simple computer architecture.", "Assembly language is advantageous in scenarios requiring low-level hardware control or optimizations.", "Open-source software allows access to its source code, promoting collaboration, while closed-source keeps the code proprietary, limiting user access."],
    }

    # Configure the layout of the GUI
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.columnconfigure(3, weight=1)
    root.columnconfigure(4, weight=1)
    root.columnconfigure(5, weight=1)

    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)
    root.rowconfigure(4, weight=1)
    root.rowconfigure(5, weight=1)
    root.rowconfigure(6, weight=1)
    root.rowconfigure(7, weight=1)
    root.rowconfigure(8, weight=1)

    # Create a "Back" button to return to the topic selection screen
    backbtn = Button(root, text="Back", font=("font2.ttf", 20), command=topicselector)
    backbtn.grid(row=8, column=0, columnspan=6)

    # Initialize the quiz for the given topics
    SiliconShowdown(root, custom_categories12, questions12, answers12)

def onethree():
    # Clear the screen or perform any necessary setup
    clear()

    # Define custom quiz categories for the first set of topics
    custom_categories13 = ["Compression, Encryption, and Hashing", "Databases", "Networks", "Web Technologies", "Transaction, Isolation, and Durability (ACID Properties)", "Network Hardware and Protocols"]

    # Define quiz questions for each category
    questions13 = {
    "Compression, Encryption, and Hashing": ["What is the difference between lossy and lossless compression?", "Explain the concepts of run length encoding and dictionary coding in lossless compression.", "Differentiate between symmetric and asymmetric encryption.", "What are the various uses of hashing in data exchange?", "Describe the role of hashing in ensuring data integrity."],
    "Databases": ["Define the terms primary key and foreign key in the context of databases.", "What is the purpose of entity relationship modeling in databases?", "Explain the concept of normalization up to 3NF.", "Interpret the term referential integrity in the context of databases.", "How does SQL contribute to data manipulation in databases?"],
    "Networks": ["Why are protocols and standards important in network communication?", "Outline the characteristics of networks.", "Explain the structure of the internet.", "How does network security address threats, and what tools are used for protection?", "Differentiate between client-server and peer-to-peer network architectures."],
    "Web Technologies": ["Define HTML, CSS, and JavaScript in the context of web development.", "Explain the process of search engine indexing.", "What is the PageRank algorithm, and how does it influence search results?", "Distinguish between server-side and client-side processing in web development.", "How do web technologies contribute to data capturing, selection, and management?"],
    "Transaction, Isolation, and Durability (ACID Properties)": ["What does ACID stand for in the context of databases?", "Explain the concept of referential integrity in database transactions.", "What is record locking, and how does it contribute to transaction management?", "How does redundancy impact data integrity in databases?", "Define the durability aspect of ACID properties in database transactions."],
    "Network Hardware and Protocols": ["Name two types of network hardware components.", "What role do firewalls play in network security?", "Explain the importance of protocols in network communication.", "What distinguishes a client-server architecture from a peer-to-peer architecture?", "How does encryption contribute to network security?"]
    }

    # Define answers for each category
    answers13 = {
    "Compression, Encryption, and Hashing": ["Lossy compression sacrifices some data to reduce file size, while lossless compression retains all original data.", "Run length encoding represents consecutive data with a symbol and count, while dictionary coding replaces patterns with shorter codes.", "Symmetric encryption uses a single key for both encryption and decryption, while asymmetric encryption uses a pair of public and private keys.", "Hashing is used for data integrity verification, password storage, and quick data retrieval.", "Hashing generates a fixed-size hash value that uniquely represents data, allowing quick verification of data integrity."],
    "Databases": ["A primary key uniquely identifies a record, while a foreign key links a record to a primary key in another table.", "Entity relationship modeling visually represents relationships between entities in a database.", "Normalization organizes data to reduce redundancy and dependency, with 3NF ensuring each non-prime attribute is non-transitively dependent on the primary key.", "Referential integrity ensures that relationships between tables remain consistent, with foreign keys matching primary keys.", "SQL (Structured Query Language) is used to interpret and modify data in relational databases."],
    "Networks": ["Protocols and standards ensure compatibility and interoperability between different systems and devices.", "Networks enable the exchange of data between devices, promoting communication and resource sharing.", "The internet is a global network of interconnected computers, following a decentralized and distributed structure.", "Network security uses firewalls, proxies, and encryption to protect against unauthorized access and data breaches.", "In a client-server architecture, a central server provides resources, while peer-to-peer involves direct communication between equal peers."],
    "Web Technologies": ["HTML structures web content, CSS styles it, and JavaScript adds interactivity to web pages.", "Search engine indexing involves analyzing and categorizing web pages to facilitate efficient search results.", "PageRank is an algorithm that assigns importance to web pages based on the number and quality of links, impacting their search engine ranking.", "Server-side processing occurs on the web server, while client-side processing happens on the user's device.", "Web technologies facilitate data capturing through forms, provide tools for data selection, and offer databases for effective data management."],
    "Transaction, Isolation, and Durability (ACID Properties)": ["ACID stands for Atomicity, Consistency, Isolation, and Durability - a set of properties ensuring reliability in database transactions.", "Referential integrity ensures that relationships between tables are maintained during database transactions, preventing inconsistencies.", "Record locking prevents simultaneous access to the same record by multiple transactions, ensuring data consistency.", "Redundancy, storing the same data in multiple places, can lead to inconsistencies and data integrity issues in databases.", "Durability ensures that once a transaction is committed, the changes made to the database persist even in the event of a system failure."],
    "Network Hardware and Protocols": ["Routers and switches are examples of network hardware components.", "Firewalls monitor and control incoming and outgoing network traffic, acting as a barrier between a trusted internal network and untrusted external networks.", "Protocols define the rules for communication between devices on a network, ensuring standardized and efficient data exchange.", "In a client-server architecture, a central server provides resources, while peer-to-peer involves direct communication between equal peers.", "Encryption protects data during transmission by converting it into a secure format, making it unreadable to unauthorized parties."]
    }

    # Configure the layout of the GUI
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.columnconfigure(3, weight=1)
    root.columnconfigure(4, weight=1)
    root.columnconfigure(5, weight=1)

    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)
    root.rowconfigure(4, weight=1)
    root.rowconfigure(5, weight=1)
    root.rowconfigure(6, weight=1)
    root.rowconfigure(7, weight=1)
    root.rowconfigure(8, weight=1)

    # Create a "Back" button to return to the topic selection screen
    backbtn = Button(root, text="Back", font=("font2.ttf", 20), command=topicselector)
    backbtn.grid(row=8, column=0, columnspan=6)
    
    # Initialize the quiz for the given topics
    SiliconShowdown(root, custom_categories13, questions13, answers13)

def onefour():
    # Clear the screen or perform any necessary setup
    clear()

    # Define custom quiz categories for the first set of topics
    custom_categories14 = ["Primitive Data Types", "Floating Point Numbers and Binary Arithmetic", "Data Structures", "Boolean Algebra", "Algorithms", "Boolean Algebra and Logic Gates"]

    # Define quiz questions for each category
    questions14 = {
    "Primitive Data Types": ["What are primitive data types, and name three examples?", "How are positive integers represented in binary?", "Explain the use of sign and magnitude in representing negative numbers in binary.", "Perform addition of the binary integers 1011 and 1101.", "Represent the decimal number 27 in hexadecimal."],
    "Floating Point Numbers and Binary Arithmetic": ["How are floating-point numbers normalized in binary?", "Perform the addition of the binary floating-point numbers 110.1 and 11.01.", "What is bitwise manipulation, and how is it used in binary operations?", "Convert the binary number 101010 to its hexadecimal equivalent.", "Explain how character sets like ASCII and UNICODE represent text."],
    "Data Structures": ["Define arrays and provide an example of a one-dimensional array.", "Name three structures used to store data and briefly describe each.", "Explain the traversal of a binary search tree.", "How do you add data to a tuple in Python?", "What is the purpose of a hash table, and how does it store data?"],
    "Boolean Algebra": ["Define Boolean logic and give an example of a problem that can be expressed using it.", "How are Boolean expressions manipulated, and what are Karnaugh maps used for?", "Apply De Morgan's Laws to the Boolean expression NOT (A AND B).", "What are the basic logic gates, and how are they represented in truth tables?", "Explain the logic associated with D-type flip-flops and half/full adders."],
    "Algorithms": ["Define algorithms and provide an example of a simple algorithm.", "Explain the concept of algorithmic complexity and its importance.", "Describe the process of binary search and its time complexity.", "What is the difference between breadth-first search and depth-first search in graph algorithms?", "How does the concept of recursion apply to algorithm design?"],
    "Boolean Algebra and Logic Gates": ["Explain the application of Boolean algebra in digital circuits.", "What are Karnaugh maps, and how are they used to simplify Boolean expressions?", "Apply De Morgan's Laws to the Boolean expression NOT (A OR B).", "Define the basic logic gates AND, OR, and NOT, and provide their truth tables.", "Explain the logic associated with D-type flip-flops and their role in sequential circuits."]
    }

    # Define answers for each category
    answers14 = {
    "Primitive Data Types": ["Primitive data types are basic data types built into programming languages. Examples include integer, real/floating point, character, string, and Boolean.", "Positive integers in binary are represented using sequences of 0s and 1s.", "Sign and magnitude represent negative numbers by using a sign bit (0 for positive, 1 for negative) and the magnitude in binary.", "1011 + 1101 = 11000", "27 in hexadecimal is 1B."],
    "Floating Point Numbers and Binary Arithmetic": ["Floating-point numbers are normalized by adjusting the binary representation to have a single non-zero digit to the left of the binary point.", "110.1 + 11.01 = 1001.11", "Bitwise manipulation involves operating on individual bits. It includes shifts and combining operations like AND, OR, and XOR.", "101010 in hexadecimal is 2A.", "ASCII and UNICODE assign unique numeric codes to characters, allowing them to be represented in a digital format."],
    "Data Structures": ["Arrays are collections of elements, and a one-dimensional array could be [1, 2, 3, 4, 5].", "Linked-list, stack, and queue are structures used to store data. A linked-list connects elements, a stack follows Last In First Out (LIFO), and a queue follows First In First Out (FIFO).", "In-order traversal involves visiting the left subtree, then the root, and finally the right subtree.", "Tuples are immutable, so you cannot add data directly. However, you can create a new tuple with additional elements.", "A hash table is used for efficient data retrieval. It stores data using a hash function that maps keys to indexes in an array."],
    "Boolean Algebra": ["Boolean logic deals with binary variables and operations. An example problem is representing the conditions for turning on a light switch.", "Boolean expressions are manipulated using rules like distribution and association. Karnaugh maps simplify Boolean expressions.", "NOT (A AND B) is equivalent to (NOT A) OR (NOT B).", "AND gate outputs true if both inputs are true, OR gate outputs true if at least one input is true, and NOT gate outputs the opposite of its input.", "D-type flip-flops store binary states and are fundamental components in sequential circuits, where the output depends not just on the current inputs but also on past inputs."],
    "Algorithms": ["Algorithms are step-by-step procedures for solving problems. An example is the algorithm to find the maximum number in a list.", "Algorithmic complexity measures the efficiency of an algorithm. It's crucial for determining the algorithm's performance as the input size increases.", "Binary search involves dividing a sorted list in half to find a target value. Its time complexity is O(log n).", "Breadth-first search explores the graph level by level, while depth-first search explores as far as possible along each branch before backtracking.", "Recursion involves a function calling itself. It's often used to solve problems by breaking them down into smaller, more manageable subproblems."],
    "Boolean Algebra and Logic Gates": ["Boolean algebra is used to design and analyze digital circuits, where logical gates process binary inputs and produce binary outputs.", "Karnaugh maps are graphical tools used to simplify Boolean expressions by grouping terms with common factors.", "NOT (A OR B) is equivalent to (NOT A) AND (NOT B).", "Routers and switches are examples of network hardware components.", "Firewalls monitor and control incoming and outgoing network traffic, acting as a barrier between a trusted internal network and untrusted external networks."]
    }

    # Configure the layout of the GUI
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.columnconfigure(3, weight=1)
    root.columnconfigure(4, weight=1)
    root.columnconfigure(5, weight=1)

    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)
    root.rowconfigure(4, weight=1)
    root.rowconfigure(5, weight=1)
    root.rowconfigure(6, weight=1)
    root.rowconfigure(7, weight=1)
    root.rowconfigure(8, weight=1)
    
    # Create a "Back" button to return to the topic selection screen
    backbtn = Button(root, text="Back", font=("font2.ttf", 20), command=topicselector)
    backbtn.grid(row=8, column=0, columnspan=6)
    
    # Initialize the quiz for the given topics
    SiliconShowdown(root, custom_categories14, questions14, answers14)

def onefive():
    # Clear the screen or perform any necessary setup
    clear()

    # Define custom quiz categories for the first set of topics
    custom_categories15 = ["Computing Legislation", "Moral and Ethical Issues in the Workforce", "Monitoring Behavior", "Cultural Impacts of Technology", "Ethical Implications of Artificial Intelligence (AI)", "Environmental Considerations in Computing"]

    # Define quiz questions for each category
    questions15 = {
    "Computing Legislation": ["What does the Data Protection Act 1998 regulate?", "Define the offenses covered by the Computer Misuse Act 1990.", "What does the Copyright Design and Patents Act 1988 protect?", "What is the purpose of the Regulation of Investigatory Powers Act 2000?", "How do these acts contribute to the legal framework for computing?"],
    "Moral and Ethical Issues in the Workforce": ["What are some moral considerations related to the use of computers in the workforce?", "Discuss the ethical implications of automated decision-making in business.", "How does the use of artificial intelligence raise moral questions?", "What environmental effects can be associated with extensive computer use?", "Explain the ethical considerations surrounding censorship and the Internet."],
    "Monitoring Behavior": ["What are the legal implications of monitoring employee behavior in the workplace?", "How can the analysis of personal information impact individuals' privacy?", "What ethical guidelines should be followed when analyzing personal information?", "Discuss the moral implications of using personal data for targeted advertising.", "What legal safeguards exist to protect individuals from improper monitoring?"],
    "Cultural Impacts of Technology": ["How does technology influence cultural norms and practices?", "Discuss the cultural challenges posed by the globalization of technology.", "Explain the role of technology in promoting cultural diversity.", "What are the ethical considerations when implementing technology in culturally diverse contexts?", "How can technology contribute to cross-cultural understanding and collaboration?"],
    "Ethical Implications of Artificial Intelligence (AI)": ["What ethical challenges arise in the development of autonomous AI systems?", "Discuss the ethical considerations in the use of AI for decision-making in healthcare.", "How can AI impact job displacement, and what ethical measures can be taken?", "Explain the ethical challenges of AI in surveillance and law enforcement.", "What ethical principles should guide the development and use of AI technologies?"],
    "Environmental Considerations in Computing": ["How does the rapid advancement of technology contribute to electronic waste?", "Discuss the environmental impact of energy consumption in data centers.", "What ethical responsibilities do tech companies have regarding environmental sustainability?", "Explain how technology can be harnessed for environmental conservation.", "What legal measures exist to regulate and enforce environmental standards in technology?"]
    }

    # Define answers for each category
    answers15 = {
    "Computing Legislation": ["The Data Protection Act 1998 regulates the processing of personal data.", "The Computer Misuse Act 1990 covers unauthorized access, modification, and related offenses.", "The Copyright Design and Patents Act 1988 protects original works.", "The Regulation of Investigatory Powers Act 2000 regulates communication interception and surveillance.", "These acts establish legal standards and consequences for various computing activities."],
    "Moral and Ethical Issues in the Workforce": ["Moral considerations may include issues related to employee privacy, fair treatment, and the impact of automation on job security.", "Ethical implications may include concerns about transparency, bias, and the impact of automated decisions on individuals.", "Moral questions may arise concerning the accountability and potential biases in AI decision-making processes.", "Environmental effects may include electronic waste, energy consumption, and the carbon footprint of data centers.", "Ethical considerations may include balancing freedom of expression with the need to prevent harm and protect individuals."],
    "Monitoring Behavior": ["Legal implications may include privacy rights and the need for informed consent in employee monitoring.", "Personal information analysis may raise concerns about unauthorized access, identity theft, and breaches of confidentiality.", "Ethical guidelines may include obtaining informed consent, ensuring data security, and transparent data practices.", "Moral implications may include concerns about manipulation, privacy invasion, and the potential for exploitation.", "Legal safeguards may include data protection laws, employment regulations, and anti-discrimination laws."],
    "Cultural Impacts of Technology": ["Technology can influence cultural norms by shaping communication, entertainment, and social interactions.", "Challenges may include the erosion of local cultures, the digital divide, and the dominance of certain cultural perspectives.", "Technology can promote cultural diversity by facilitating communication, preserving languages, and providing platforms for diverse voices.", "Ethical considerations may include respecting cultural values, avoiding cultural appropriation, and ensuring inclusive technology design.", "Technology can facilitate cross-cultural understanding through online platforms, language translation, and virtual communication."],
    "Ethical Implications of Artificial Intelligence (AI)": ["Challenges may include accountability, transparency, and ensuring that AI systems align with human values.", "Ethical considerations may include patient consent, fairness in treatment recommendations, and avoiding bias in healthcare AI systems.", "AI can lead to job displacement, and ethical measures may include retraining programs, social safety nets, and responsible AI deployment.", "Challenges may include privacy concerns, bias in facial recognition, and the potential misuse of AI in surveillance.", "Ethical principles may include transparency, fairness, accountability, and a focus on human well-being."],
    "Environmental Considerations in Computing": ["Rapid technology advancement can lead to the disposal of outdated electronic devices, contributing to electronic waste.", "Data centers consume significant energy, contributing to carbon emissions and environmental impact.", "Tech companies have a responsibility to adopt sustainable practices, reduce electronic waste, and minimize their carbon footprint.", "Technology can be used for environmental conservation through data monitoring, sustainable practices, and innovations in renewable energy.", "Legal measures may include environmental regulations, waste disposal laws, and incentives for eco-friendly practices in technology."]
    }

    # Configure the layout of the GUI
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.columnconfigure(3, weight=1)
    root.columnconfigure(4, weight=1)
    root.columnconfigure(5, weight=1)

    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)
    root.rowconfigure(4, weight=1)
    root.rowconfigure(5, weight=1)
    root.rowconfigure(6, weight=1)
    root.rowconfigure(7, weight=1)
    root.rowconfigure(8, weight=1)

    # Create a "Back" button to return to the topic selection screen
    backbtn = Button(root, text="Back", font=("font2.ttf", 20), command=topicselector)
    backbtn.grid(row=8, column=0, columnspan=6)
    
    # Initialize the quiz for the given topics
    SiliconShowdown(root, custom_categories15, questions15, answers15)

def twoone():
    # Clear the screen or perform any necessary setup
    clear()

    # Define custom quiz categories for the first set of topics
    custom_categories21 = ["Abstract Thinking", "Thinking Ahead", "Thinking Procedurally", "Thinking Logically", "Thinking Concurrently", "Legal and Ethical Considerations"]

    # Define quiz questions for each category
    questions21 = {
    "Abstract Thinking": ["What is the nature of abstraction in computational thinking?", "Why is there a need for abstraction in computational problem-solving?", "Explain the differences between an abstraction and reality.", "How do you devise an abstract model for various situations?", "Discuss scenarios where abstraction is beneficial in computational thinking."],
    "Thinking Ahead": ["How do you identify inputs and outputs for a given situation in computational thinking?", "What are preconditions, and why are they important in problem-solving?", "Discuss the nature, benefits, and drawbacks of caching in computational thinking.", "Why is the need for reusable program components crucial in computational design?", "Explain the steps involved in determining sub-procedures to solve a problem."],
    "Thinking Procedurally": ["What does it mean to identify the components of a problem procedurally?", "How do you determine the order of steps needed to solve a problem procedurally?", "Why is it important to identify sub-procedures in computational thinking?", "Provide an example of a problem and identify its sub-procedures.", "Discuss the significance of recognizing components and sub-procedures in problem-solving."],
    "Thinking Logically": ["How do you identify decision points in a solution logically?", "Determine the logical conditions that affect the outcome of a decision.", "How do decisions affect the flow through a program logically?", "Provide an example of a decision-making scenario in computational thinking.", "Discuss the role of logical thinking in creating effective program flow."],
    "Thinking Concurrently": ["How do you determine parts of a problem that can be tackled concurrently?", "Outline the benefits of concurrent processing in a particular situation.", "What trade-offs might arise from concurrent processing in specific scenarios?", "Provide an example where concurrent thinking can enhance problem-solving.", "Discuss the importance of considering benefits and trade-offs in concurrent processing."],
    "Legal and Ethical Considerations": ["Explain the significance of ethical considerations in computational thinking.", "What is the Data Protection Act 1998, and why is it important?", "Discuss the Computer Misuse Act 1990 and its implications.", "Explain the role of the Copyright, Design, and Patents Act 1988 in computing.", "What is the Regulation of Investigatory Powers Act 2000, and how does it impact computing?"]
    }   

    # Define answers for each category
    answers21 = {
    "Abstract Thinking": ["Abstraction involves simplifying complex concepts.", "Abstraction is necessary to manage complexity.", "An abstraction is a simplified representation.", "Create an abstract model by identifying key aspects.", "Abstraction is beneficial in handling large-scale systems."],
    "Thinking Ahead": ["Identify inputs by recognizing necessary information.", "Preconditions set the context and constraints.", "Caching improves performance with potential drawbacks.", "Reusable components save time and promote modularity.", "Determine steps for each sub-procedure to solve a problem."],
    "Thinking Procedurally": ["Procedural thinking involves breaking down a problem.", "Determine the logical sequence of steps.", "Identifying sub-procedures facilitates an organized approach.", "For sorting, sub-procedures may include comparing and swapping.", "Recognizing components enhances clarity and efficiency."],
    "Thinking Logically": ["Identify decision points by recognizing situations for choices.", "Logical conditions include factors influencing decisions.", "Decisions direct program flow based on logical conditions.", "In a weather app, decisions might involve temperature checks.", "Logical thinking ensures programs respond appropriately."],
    "Thinking Concurrently": ["Concurrent thinking involves identifying independent components.", "Benefits include improved efficiency and reduced execution time.", "Trade-offs may include increased complexity and synchronization issues.", "In a web server, concurrent processing handles multiple requests.", "Considering benefits and trade-offs helps determine appropriateness."],
    "Legal and Ethical Considerations": ["Ethical considerations address moral dilemmas in computing.", "The Data Protection Act 1998 regulates personal data processing.", "The Computer Misuse Act 1990 criminalizes unauthorized access.", "The Copyright, Design, and Patents Act 1988 protects intellectual property.", "The Regulation of Investigatory Powers Act 2000 balances surveillance and privacy."]
    }

    # Configure the layout of the GUI
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.columnconfigure(3, weight=1)
    root.columnconfigure(4, weight=1)
    root.columnconfigure(5, weight=1)

    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)
    root.rowconfigure(4, weight=1)
    root.rowconfigure(5, weight=1)
    root.rowconfigure(6, weight=1)
    root.rowconfigure(7, weight=1)
    root.rowconfigure(8, weight=1)
    
    # Create a "Back" button to return to the topic selection screen
    backbtn = Button(root, text="Back", font=("font2.ttf", 20), command=topicselector)
    backbtn.grid(row=8, column=0, columnspan=6)
    
    # Initialize the quiz for the given topics
    SiliconShowdown(root, custom_categories21, questions21, answers21)

def twotwo():
    # Clear the screen or perform any necessary setup
    clear()

    # Define custom quiz categories for the first set of topics
    custom_categories22 = ["Programming Constructs", "Recursion and Iteration", "Variables and Modularity", "IDE Usage", "Object-Oriented Techniques", "Computational Methods"]

    # Define quiz questions for each category
    questions22 = {
    "Programming Constructs": ["What are the basic programming constructs?", "Explain the significance of sequence in programming.", "How does iteration contribute to solving problems in programming?", "Discuss the role of branching in programming.", "Provide an example of using programming constructs in problem-solving."],
    "Recursion and Iteration": ["Define recursion in programming.", "Compare recursion to an iterative approach.", "How can recursion be used in problem-solving?", "Explain the concept of global and local variables.", "Discuss scenarios where recursion is more suitable than iteration."],
    "Variables and Modularity": ["Differentiate between global and local variables.", "Explain the concept of modularity in programming.", "What are functions and procedures in programming?", "Discuss parameter passing by value and by reference.", "How does modularity contribute to writing maintainable code?"],
    "IDE Usage": ["What is the role of an Integrated Development Environment (IDE) in programming?", "How does an IDE assist in program development?", "Discuss the importance of debugging in programming.", "Explain how learners can use an IDE for program development.", "Provide examples of popular IDEs used in programming."],
    "Object-Oriented Techniques": ["Define object-oriented programming (OOP) techniques.", "Explain the concept of classes and objects in OOP.", "Discuss the role of inheritance in object-oriented programming.", "What is encapsulation in the context of OOP?", "How do learners apply object-oriented techniques in problem-solving?"],
    "Computational Methods": ["Identify features that make a problem solvable by computational methods.", "Explain the importance of problem recognition in computational methods.", "Discuss the steps involved in problem decomposition.", "How is the 'divide and conquer' approach used in computational methods?", "Explain the role of abstraction in computational problem-solving."]
    }

    # Define answers for each category
    answers22 = {
    "Programming Constructs": ["Sequence, iteration, branching", "Sequence ensures ordered execution.", "Iteration repeats a block of code.", "Branching facilitates decision-making.", "Example: Writing a simple calculator program."],
    "Recursion and Iteration": ["Recursion involves a function calling itself.", "Recursion vs. iteration comparison.", "Recursion solves problems via self-replication.", "Global variables are accessible everywhere; local variables have limited scope.", "Example: Recursive factorial calculation."],
    "Variables and Modularity": ["Global variables are accessible throughout the program; local variables have limited scope.", "Modularity breaks a program into manageable parts.", "Functions and procedures are reusable code segments.", "Parameter passing methods influence variable scope.", "Modularity aids code organization and maintenance."],
    "IDE Usage": ["IDEs provide tools for program development.", "IDEs assist in writing, testing, and debugging code.", "Debugging is crucial for identifying and fixing errors.", "Learners can use an IDE for coding, testing, and debugging.", "Examples include Visual Studio, PyCharm, and Eclipse."],
    "Object-Oriented Techniques": ["OOP uses classes and objects to structure code.", "Classes define blueprints for objects.", "Inheritance allows a class to inherit properties from another.", "Encapsulation hides the internal workings of an object.", "Learners apply OOP for organized and modular code."],
    "Computational Methods": ["Certain features make problems suitable for computational solutions.", "Problem recognition is crucial for effective problem-solving.", "Problem decomposition breaks complex problems into smaller parts.", "Divide and conquer addresses problems by breaking them into smaller sub-problems.", "Abstraction simplifies complex problems for better understanding."]
    }

    # Configure the layout of the GUI
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.columnconfigure(3, weight=1)
    root.columnconfigure(4, weight=1)
    root.columnconfigure(5, weight=1)

    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)
    root.rowconfigure(4, weight=1)
    root.rowconfigure(5, weight=1)
    root.rowconfigure(6, weight=1)
    root.rowconfigure(7, weight=1)
    root.rowconfigure(8, weight=1)
    
    # Create a "Back" button to return to the topic selection screen
    backbtn = Button(root, text="Back", font=("font2.ttf", 20), command=topicselector)
    backbtn.grid(row=8, column=0, columnspan=6)
    
    # Initialize the quiz for the given topics
    SiliconShowdown(root, custom_categories22, questions22, answers22)

def twothree():
    # Clear the screen or perform any necessary setup
    clear()

    # Define custom quiz categories for the first set of topics
    custom_categories23 = ["Algorithm Analysis", "Algorithm Suitability", "Efficiency Measures", "Complexity Comparison", "Data Structure Algorithms", "Standard Algorithms"]

    # Define quiz questions for each category
    questions23 = {
    "Algorithm Analysis": ["What is involved in the analysis and design of algorithms?", "How do algorithms contribute to problem-solving in a given situation?", "Discuss the importance of algorithm analysis for efficient solutions.", "Explain the role of algorithms in handling specific tasks and data sets.", "Why is algorithm design crucial for effective problem-solving?"],
    "Algorithm Suitability": ["How do you determine the suitability of different algorithms for a specific task?", "In what terms is algorithm suitability evaluated?", "Discuss the factors influencing the choice of algorithms for a given data set.", "Explain the significance of execution time in algorithm suitability.", "Why is space complexity an essential consideration in algorithm selection?"],
    "Efficiency Measures": ["What measures are used to determine the efficiency of different algorithms?", "Explain the concept of Big O notation.", "Discuss different complexities in Big O notation (constant, linear, polynomial, exponential, logarithmic).", "How does constant complexity differ from logarithmic complexity?", "Why is efficiency crucial in algorithm design and selection?"],
    "Complexity Comparison": ["Why is it important to compare the complexity of algorithms?", "What factors are considered when comparing algorithm complexities?", "Explain the significance of polynomial complexity in algorithm comparison.", "How does exponential complexity differ from linear complexity?", "Discuss the trade-offs involved in choosing between algorithms with different complexities."],
    "Data Structure Algorithms": ["Discuss the algorithms associated with main data structures (stacks, queues, trees, linked lists).", "How are depth-first and breadth-first traversal applied to trees?", "Explain the process of post-order traversal of trees.", "Why is breadth-first traversal commonly used in certain scenarios?", "How do algorithms contribute to the manipulation and traversal of data structures?"],
    "Standard Algorithms": ["Discuss the standard algorithms commonly used in computer science.", "Explain the working principles of bubble sort and insertion sort algorithms.", "How does merge sort differ from quick sort in terms of operation?", "Discuss the applications of Dijkstra's shortest path algorithm.", "Explain the principles behind the A* algorithm for pathfinding."]
    }

    # Define answers for each category
    answers23 = {
    "Algorithm Analysis": ["Analysis and design of algorithms involve planning and structuring problem-solving approaches.", "Algorithms provide systematic and step-by-step solutions for a given situation.", "Algorithm analysis is crucial for optimizing solutions and improving efficiency.", "Algorithm design is essential for breaking down complex problems into manageable steps.", "Effective problem-solving requires a thoughtful approach to algorithm design."],
    "Algorithm Suitability": ["Suitability is determined by evaluating algorithms for specific tasks.", "Algorithm suitability is evaluated in terms of factors like execution time and space complexity.", "Factors influencing algorithm choice include data set characteristics and problem requirements.", "Execution time is crucial for real-time applications, influencing algorithm suitability.", "Space complexity considerations ensure optimal resource utilization in algorithm selection."],
    "Efficiency Measures": ["Efficiency measures include factors like execution time and space complexity.", "Big O notation provides a standardized way to express algorithm efficiency.", "Big O notation covers complexities such as constant, linear, polynomial, exponential, and logarithmic.", "Constant complexity implies a consistent execution time, while logarithmic complexity scales with the logarithm of input size.", "Efficiency is vital to ensure optimal algorithm performance in different scenarios."],
    "Complexity Comparison": ["Comparing complexity helps in selecting the most suitable algorithm for a given problem.", "Factors considered in complexity comparison include execution time and resource usage.", "Polynomial complexity involves algorithms whose performance is influenced by polynomial functions.", "Exponential complexity grows rapidly with input size, contrasting with linear complexity.", "Choosing between different complexities involves considering trade-offs and application requirements."],
    "Data Structure Algorithms": ["Algorithms are applied to manipulate and traverse main data structures like stacks, queues, trees, and linked lists.", "Depth-first and breadth-first traversal techniques are used in tree manipulation.", "Post-order traversal involves visiting the nodes of a tree after their subtrees.", "Breadth-first traversal is commonly used to explore neighbor nodes at the current depth prior to moving on.", "Algorithms enhance the efficiency of data structure manipulation and traversal."],
    "Standard Algorithms": ["Standard algorithms are widely accepted solutions to common problems in computer science.", "Bubble sort and insertion sort algorithms involve comparing and rearranging elements in a list.", "Merge sort and quick sort differ in their approaches to sorting elements in a list.", "Dijkstra's shortest path algorithm finds the shortest paths between nodes in a graph.", "The A* algorithm is a heuristic-based approach commonly used in pathfinding applications."]
    }

    # Configure the layout of the GUI
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.columnconfigure(3, weight=1)
    root.columnconfigure(4, weight=1)
    root.columnconfigure(5, weight=1)

    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)
    root.rowconfigure(4, weight=1)
    root.rowconfigure(5, weight=1)
    root.rowconfigure(6, weight=1)
    root.rowconfigure(7, weight=1)
    root.rowconfigure(8, weight=1)
    
    # Create a "Back" button to return to the topic selection screen 
    backbtn = Button(root, text="Back", font=("font2.ttf", 20), command=topicselector)
    backbtn.grid(row=8, column=0, columnspan=6)
    
    # Initialize the quiz for the given topics
    SiliconShowdown(root, custom_categories23, questions23, answers23)

def lightmode():
    # Function to set the root background color to a light mode color
    root.configure(bg=mycolour2)

def darkmode():
    # Function to set the root background color to a dark mode color
    root.configure(bg=mycolour)

def options():
    # Function to display the Options screen
    
    # Clear the screen or perform any necessary setup
    clear()

    # Set the title of the window
    root.title("Silicon Showdown - Options")

    # Create buttons for light mode, dark mode, and back
    lightmodebtn = Button(root, text="Light Mode", command=lightmode, font=("LEMONMILK-Regular.otf", 40), width=10, height=2)
    darkmodebtn = Button(root, text="Dark Mode", command=darkmode, font=("LEMONMILK-Regular.otf", 40), width=10, height=2)
    backbtn = Button(root, text="Back", font=("font2.ttf", 20), command=main_menu)

    # Pack buttons to be displayed with specified padding
    lightmodebtn.pack(side='top', padx=10, pady=10)
    darkmodebtn.pack(side='top', padx=10, pady=10)
    backbtn.pack(side='top', padx=10, pady=10)

def about():
    # Function to display the About screen
    
    # Clear the screen
    clear()

    # Set the title of the window
    root.title("Silicon Showdown - About")

    # About text providing information about the game
    about_text = "Silicon Showdown is a trivia quiz game that tests your knowledge of computer science and technology. \n" \
                 "You can choose from various topics and answer questions to earn points. \n" \
                 "The game is designed to be both fun and educational. \n" \
                 "Good luck and enjoy!"

    # Create label to display the about text with specified font and wrapping
    about_label = Label(root, text=about_text, font=("font2.ttf", 50), wraplength=800, justify="left")
    
    # Create a button to go back to the main menu
    backbtn = Button(root, text="Back", font=("font2.ttf", 20), command=main_menu)

    # Pack label and button to be displayed with specified padding
    about_label.pack(side='top', padx=10, pady=10)
    backbtn.pack(side='top', padx=10, pady=10)

def easteregg():
    # Function to display the Easter Egg screen
    
    # Clear the screen
    clear()

    # Set the title of the window
    root.title("Silicon Showdown - ???")

    # Configuring the columns and rows weights for better layout
    for i in range(6):
        root.columnconfigure(i, weight=1)
    for i in range(9):
        root.rowconfigure(i, weight=1)

    # Creating 54 Back buttons with 'main_menu' command
    back_buttons = [Button(root, text="Back", command=joke) for _ in range(54)]

    # Distributing the buttons in a 6x9 grid
    for i in range(9):
        for j in range(6):
            back_buttons[i * 6 + j].grid(row=i, column=j)

def joke():
    # Function to display the Joke screen
    
    # Clear the screen
    clear()

    # Create a StringVar to hold the joke text
    joke_text = StringVar()

    # Create a label to display the joke text with specified font size
    joke_label = Label(root, textvariable=joke_text, font=("font2.ttf", 30))
    joke_label.pack(pady=20)

    # Create a button to fetch a new joke
    fetch_button = Button(root, text="Get Joke", command=lambda: fetch_joke(joke_text), font=("LEMONMILK-Regular.otf", 20), width=10, height=2)
    fetch_button.pack()

    # Create a back button to return to the main menu
    backbtn = Button(root, text="Back", command=main_menu, font=("LEMONMILK-Regular.otf", 10), width=5, height=1)
    backbtn.pack(side='top', padx=10, pady=10)

def fetch_joke(joke_text):
    # Function to fetch a programming joke and display it
    
    # Make a GET request to the joke API
    response = requests.get("https://official-joke-api.appspot.com/jokes/programming/random")
    
    # Parse the JSON response to get joke data
    joke_data = response.json()[0]
    
    # Set the joke text to display setup and punchline
    joke_text.set(joke_data['setup'] + '\n' + joke_data['punchline'])

# Initial call to the main menu function
main_menu()

# Start the Tkinter event loop
root.mainloop()