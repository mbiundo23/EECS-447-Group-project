# Import neccessary modules
import string

# All possible resource types
RESOURCE_TYPES = ["PhysicalBook", "eBook", "AudioBook", "Magazine", "Equipment", "DigitalDisk"]

# All possible equipment models.
EQUIPMENT_MODELS = [
    "MacBook Pro 13-inch",
    "iPad Pro 12.9-inch",
    "Sony WH-1000XM5 Headphones",
    "Anker PowerCore 26800 Portable Charger",
    "Epson EF-100 Mini-Laser Projector",
    "iPhone 15 Pro",
    "Kindle Paperwhite E-Reader",
    "Ultimaker S3 3D Printer",
    "Oculus Quest 2 VR Headset",
    "Canon EOS Rebel T7 DSLR Camera",
    "Blue Yeti USB Microphone",
    "Sony HDR-CX405 Camcorder",
    "Amazon Echo Dot Smart Speaker",
    "Seagate Backup Plus 1TB External Hard Drive",
    "Wacom Intuos Pro Graphics Tablet",
    "DJI Mini 2 Drone",
    "Nintendo Switch Gaming Console",
    "Fujitsu ScanSnap iX1500 Document Scanner",
    "Fitbit Charge 5 Smartwatch",
    "MakerBot Replicator+ 3D Printer",
    "Microsoft Surface Pro 7",
    "Apple Watch Series 8",
    "Samsung Galaxy S23",
    "Logitech MX Master 3 Mouse",
    "BenQ 32-inch 4K Monitor",
    "GoPro HERO11 Black",
    "Bose QuietComfort 45 Headphones",
    "Dyson V15 Detect Cordless Vacuum",
    "Samsung T7 Portable SSD",
    "Acer Predator Helios 300 Laptop"
]

# All possible first names.
FIRST_NAMES = [
    "James", "Mary", "John", "Patricia", "Robert", 
    "Jennifer", "Michael", "Linda", "William", "Elizabeth",
    "David", "Emma", "Daniel", "Sophia", "Matthew", 
    "Olivia", "Joshua", "Liam", "Ethan", "Isabella", 
    "Lucas", "Charlotte", "Mason", "Amelia", "Benjamin", 
    "Harper", "Jackson", "Chloe", "Henry", "Avery"
]

# All possible middle initials inluding empty initial.
MIDDLE_INITIALS = [""] + list(string.ascii_uppercase)

# All possible last names.
LAST_NAMES = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", 
    "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Taylor", "Anderson", "Thomas", "Jackson", "White", 
    "Harris", "Martin", "Thompson", "Lee", "Gonzalez", 
    "Perez", "Wilson", "Clark", "Lewis", "Young", 
    "Walker", "Hall", "Allen", "King", "Scott", "Green"
]
# All possible genres.
GENRES = [
    "Fantasy",
    "Science Fiction",
    "Mystery",
    "Thriller",
    "Romance",
    "Historical Fiction",
    "Horror",
    "Young Adult",
    "Adventure",
    "Dystopian",
    "Contemporary",
    "Magical Realism",
    "Literary Fiction",
    "Crime",
    "Biography",
    "Autobiography",
    "Self-Help",
    "Humor",
    "Political Fiction",
    "Paranormal",
    "Graphic Novel"
]

# All possible magazine genres.
MAGAZINE_GENRES = [
    "Fashion",
    "Lifestyle",
    "Technology",
    "Science",
    "Health and Fitness",
    "Business",
    "Travel",
    "Food and Cooking",
    "Sports",
    "Entertainment",
    "Art and Design",
    "Home and Garden",
    "Parenting",
    "Automotive",
    "Photography"
]

# All possible digital disk types.
DIGITAL_DISK_TYPES = [
    "CD",       
    "DVD",      
    "Blu-ray", 
    "HD DVD",   
    "MiniDisc", 
    "LaserDisc" 
]

# All possible media types.
MEDIA_TYPES = [
    "Audio",          
    "Video",       
    "Data",         
    "Game",         
    "Photos",         
    "Educational",    
    "Archival",       
    "Interactive",  
    "Hybrid",      
]   

# All possible adjectives for generating resource titles.
ADJECTIVES = [
    "Mystic", "Silent", "Forgotten", "Endless", "Shattered", 
    "Hidden", "Dark", "Eternal", "Broken", "Radiant", 
    "Cursed", "Whispering", "Fading", "Forsaken", "Crimson", 
    "Lost", "Unspoken", "Haunting", "Enchanted", "Ancient",
    "Luminous", "Glimmering", "Fierce", "Blazing", "Majestic",
    "Sacred", "Shimmering", "Timeless", "Serene", "Fiery",
    "Invisible", "Lurking", "Epic", "Sublime", "Wicked",
    "Ancient", "Frosted", "Spectral", "Burnished", "Arcane",
    "Imposing", "Mighty", "Fragrant", "Cavernous", "Celestial"
]


# All possible base words for generating resource titles.
BASEWORDS = [
    "Journey", "Secret", "Dream", "World", "Night", 
    "Path", "Legend", "Shadow", "Realm", "Heart", 
    "Soul", "Empire", "Throne", "Mystery", "Quest", 
    "Wings", "Fate", "Chronicles", "Tale", "Kingdom", 
    "Rise", "Darkness", "Light", "Vengeance", "Power", 
    "Hope", "Victory", "Terror", "Storm", "Legacy", 
    "Valor", "Destiny", "Revenge", "Phoenix", "Odyssey",
    "Vow", "Rebirth", "Endeavor", "Horizon", "Eclipse", 
    "Enigma", "Conquest", "Arcadia", "Freedom", "Triumph"
]

# All possible publishers for resources.
PUBLISHERS = [
    "Penguin Random House", "HarperCollins", "Simon & Schuster", 
    "Macmillan", "Hachette Book Group", "Oxford University Press", 
    "Wiley", "Pearson", "Springer", "Bloomsbury", 
    "Scholastic", "Random House", "Capstone", "Routledge", 
    "Prentice Hall", "University of Chicago Press", "Cengage", 
    "Cambridge University Press", "Northwestern University Press", 
    "Harvard University Press"
]

# All possible Distributors for digital disk.
DISTRIBUTORS = [
    "Warner Music Group",
    "Universal Music Group",
    "Sony Music Entertainment",
    "Paramount Pictures",
    "20th Century Studios",
    "Lionsgate",
    "Disney Media Distribution",
    "MGM Studios",
    "Netflix",
    "Hulu",
    "Amazon Prime Video",
    "Apple TV+",
    "Vudu",
    "Redbox",
    "Best Buy",
    "Target",
    "Walmart",
    "FYE (For Your Entertainment)",
    "Barnes & Noble",
    "CD Projekt"
]
# All possible membership types.
MEMBERSHIP_TYPES = ["Regular", "Student", "Senior"]

# Earliest publication year
EARLIEST_PUBLICATION_YEAR = 2000

# Max authors assigned to a resource
MAX_AUTHORS = 5

# Age to be considered a senior.
SENIOR_AGE = 65

# CONSTANTS RESPONSIBLE FOR POPULATING DATA
NUMBER_OF_RESOURCES = 500
NUMBER_OF_AUTHORS = 50
NUMBER_OF_MEMBERS = 100
NUMBER_OF_BORROWS = 1000

NUMBER_OF_ROOMS = 50
MIN_CAPACITY = 1
MAX_CAPACITY = 50
NUMBER_OF_RESERVATIONS = 250