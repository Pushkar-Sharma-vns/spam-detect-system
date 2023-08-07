import random
from account.models import User
from contacts.models import ContactList


def populate_users():
    random_names = [
        "Emma", "Noah", "Olivia", "Liam", "Ava", "Isabella", "Sophia", "Mia", "Charlotte", "Amelia",
        "Harper", "Evelyn", "Abigail", "Emily", "Elizabeth", "Mila", "Ella", "Avery", "Sofia", "Camila",
        "Aria", "Scarlett", "Victoria", "Madison", "Luna", "Grace", "Chloe", "Penelope", "Layla", "Riley",
        "Zoey", "Nora", "Lily", "Eleanor", "Hannah", "Lillian", "Addison", "Aubrey", "Ellie", "Stella",
        "Natalie", "Zoe", "Leah", "Hazel", "Violet", "Aurora", "Savannah", "Audrey", "Brooklyn", "Bella",
        "Claire", "Skylar", "Lucy", "Paisley", "Everly", "Anna", "Caroline", "Nova", "Genesis", "Emilia",
        "Kennedy", "Samantha", "Maya", "Willow", "Kinsley", "Naomi", "Aaliyah", "Elena", "Sarah", "Ariana",
        "Allison", "Gabriella", "Alice", "Madelyn", "Cora", "Ruby", "Eva", "Serenity", "Autumn", "Adeline",
        "Hailey", "Gianna", "Valentina", "Isla", "Eliana", "Quinn", "Nevaeh", "Ivy", "Sadie", "Piper",
        "Lydia", "Alexa", "Josephine", "Emery", "Julia", "Delilah", "Arianna", "Vivian", "Kaylee", "Sophie",
        "Brielle", "Madeline", "Peyton", "Rylee", "Clara", "Hadley", "Melanie", "Mackenzie", "Reagan",
        "Adalynn", "Liliana", "Aubree", "Jade", "Katherine", "Isabelle", "Natalia", "Raelynn", "Maria",
        "Athena", "Ximena", "Ayla", "Leilani", "Taylor", "Faith", "Rose", "Kylie", "Alexandra", "Mary",
        "Margaret", "Lyla", "Ashley", "Amaya", "Eliza", "Brianna", "Bailey", "Andrea", "Khloe", "Jasmine",
        "Melody", "Iris", "Isabel", "Norah", "Annabelle", "Valeria", "Emerson", "Adalyn", "Ryleigh",
        "Eden", "Emersyn", "Anastasia", "Kayla", "Alyssa", "Juliana", "Charlie", "Esther", "Ariel",
        "Cecilia", "Valerie", "Alina", "Molly", "Reese", "Aliyah", "Lilly", "Parker", "Finley", "Morgan",
        "Sydney", "Jordyn", "Eloise", "Trinity", "Daisy", "Kimberly", "Lauren", "Genevieve", "Sara",
        "Arabella", "Harmony", "Elise", "Remi", "Teagan", "Alexis", "London", "Sloane", "Laila", "Lucia",
        "Diana", "Juliette", "Sienna", "Elliana", "Londyn", "Ayla", "Callie", "Gracie", "Josie", "Amara",
        "Jocelyn", "Daniela", "Everleigh", "Mya", "Rachel", "Summer", "Alana", "Brooke", "Alaina",
        "Mckenzie", "Catherine", "Amy", "Presley", "Journee", "Rosalie", "Ember", "Brynlee", "Rowan",
        "Joanna", "Paige", "Rebecca", "Ana", "Sawyer", "Mariah", "Nicole", "Brooklynn", "Payton", "Marley",
        "Fiona", "Georgia", "Lila", "Harley", "Adelyn", "Alivia", "Noelle", "Gemma", "Vanessa", "Journey",
        "Makayla", "Angelina", "Adaline", "Catalina", "Alayna", "Julianna", "Leila", "Lola", "Adriana",
        "June", "Juliet", "Jayla", "River", "Tessa", "Lia", "Dakota", "Delaney", "Selena", "Blakely",
        "Ada", "Camille", "Zara", "Malia", "Hope", "Samara", "Vera", "Mckenna", "Briella", "Izabella",
        "Hayden", "Raegan", "Michelle", "Angela", "Ruth", "Freya", "Kamila", "Vivienne", "Aspen", "Olive",
        "Kendall", "Elaina", "Thea", "Kali", "Destiny", "Amiyah", "Evangeline", "Cali", "Blake", "Elsie",
        "Juniper", "Alexandria", "Myla", "Ariella", "Kate", "Mariana", "Lilah", "Charlee", "Daleyza",
        "Nyla", "Jane", "Maggie", "Zuri", "Aniyah", "Lucille", "Leia", "Melissa", "Adelaide", "Amina",
        "Giselle", "Lena", "Camilla", "Miriam", "Millie", "Brynn", "Gabrielle", "Sage", "Annie", "Logan",
        "Lilliana", "Haven", "Jessica", "Kaia", "Magnolia", "Amira", "Adelynn", "Makenzie", "Stephanie",
        "Nina", "Phoebe", "Arielle", "Evie", "Lyric", "Alessandra", "Gabriela", "Paislee", "Raelyn",
        "Madilyn", "Paris", "Makenna", "Kinley", "Gracelyn", "Talia", "Maeve", "Rylie", "Kiara", "Evelynn",
        "Brinley", "Jacqueline", "Laura", "Gracelynn", "Lexi", "Ariah", "Fatima", "Jennifer", "Kehlani",
        "Alani", "Ariyah", "Luciana", "Allie", "Heidi", "Maci", "Phoenix", "Felicity", "Joy", "Kenzie",
        "Veronica", "Margot", "Addilyn", "Lana", "Cassidy", "Remington", "Saylor", "Ryan", "Keira",
        "Harlow", "Miranda", "Angel", "Amanda", "Danielle", "Dylan", "Ainsley", "Kiari", "Remedy",
        "Alexia", "Sierra", "Jordan", "Harper", "Peyton", "Brynlee", "Gwen", "Ireland", "Maddison",
        "Mila", "Presley", "Juliet", "Leilani", "Jayleen", "Miracle", "Reign", "Amari", "Juliette",
        "Meadow", "Sunny", "Fiona", "Kori", "Alaya", "Lyra", "Skylar", "Annika", "Hermione", "Beatrice",
        "Eliora", "Scarlet", "Nalani", "Waverly", "Zayla", "Liana", "Alaiya", "Milani", "Yara", "Tenley",
        "Aviana", "Astrid", "Noa", "Roselyn", "Zora", "Lilith", "Linda", "Estelle", "Rhea", "Livia",
        "Celeste", "Aitana", "Kenna", "Barbara", "Andi", "Goldie", "Tinley", "Marjorie", "Maxine", "Kimora",
        "Amalia", "Lara", "Karina", "Cara", "Leighton", "Nellie", "Nala", "Emmeline", "Amelie", "Aislinn",
        "Elora", "Hanna", "Kathleen", "Mireya", "Melany", "Priscilla", "Siena", "Karter", "Rosalyn",
        "Clarissa", "Galilea", "Aliana", "Belen", "Florence", "Gloria", "Katie", "Malaya", "Wren", "Zaniyah",
        "Aubriella", "Belle", "Bexley", "Kyla", "Mikaela", "Esperanza", "Zariah", "Skyla", "Dulce",
        "Bellamy", "Veda", "Lincoln", "Lainey", "Adele", "Nalani", "Elisabeth", "Rosalind", "Renee", "Dalary",
        "Fantasia", "Vanessa", "Jayda", "Angeline", "Anahi", "Kenia", "Kamilah", "Yareli", "Celine",
        "Halle", "Laylah", "Jamie", "Jaelyn", "Kiera", "Tegan", "Lillianna", "Imani", "Yaretzi", "Moriah",
        "Bria", "Leyla", "Ellis", "Holly", "Emilee", "Jaycee", "Karter", "Lorelei", "Miah", "Charleigh",
        "Remington", "Ellianna", "Kori", "Elina", "Karlee", "Cynthia", "Armani", "Avalyn", "Marianna",
        "Miley", "Jolene", "Alayah", "Bethany", "Teresa", "Adilynn", "Kora", "Cecelia", "Aleah", "Lylah",
        "Joyce", "Allyson", "Jazmine", "Myra", "April", "Magdalena", "Emerie", "Coraline", "Reyna",
        "Rory", "Laylani", "Kairi", "Tori", "Dayana", "Mavis", "Sutton", "Anika", "Zola", "Mariam", "Kara",
        "Kailani", "Joslyn", "Mae", "Reina", "Brenda", "Monroe", "Aniya", "Emmalyn", "Kyra", "Riya", "Braylee",
        "Livia", "Lilith", "Amaris", "Anya", "Kai", "Dallas", "Cara", "Estella", "Milena", "Aubrielle",
        "Jaelynn", "Navy", "Ryann", "Princess", "Sariah", "Taliyah", "Arlette", "Bexley", "Cataleya",
        "Kailyn", "Mikaela", "Alma", "Estrella", "Rivka", "Aadhya", "Aliza", "Myla", "Emmeline", "Itzayana",
        "Kensley", "Milana", "Kylan", "Mariana", "Amayah", "Carolina", "Elaine", "Alena", "Laurel", "Jemma",
        "Addyson", "Greta", "Charley", "Ellen", "Florence", "Kristina", "Averie", "Elisa", "Ram", "Shyam"
    ]
    

    random_phones = ['+916120747770','+916511188399','+917979052142','+916570802305','+918700916225','+916127911800','+917979786985','+917288865341','+916127944463','+918079832052','+916128154058','+918079020861','+916809411046','+916127918484','+916809915833','+916127901642','+918917765309','+916127922795','+916127921789','+916127935753','+916127988924','+916127999246','+917887731375','+918701328458','+916710399401','+917319682003','+918207206911','+916127942844','+916127995969','+918919530377','+916127953234','+917887639812','+916127919681','+916127928185','+916127941400','+916127977468','+916409634309','+916579911853','+916127912354','+918847556119','+916127930033','+917887425947','+917931360820','+918709870460','+918707182494','+916740019004','+916518994084','+917931302385','+917277131911','+916127908569','+917192024081','+916219893751','+916127900124','+916127988645','+918217293634','+916127984906','+918070635826','+917289817498','+918217381332','+916128830892','+918079562882','+918709994659','+916933314035','+916127902566','+916127943315','+918844882725','+916318077216','+916127981076','+916127921628','+917979096697','+916127939233','+916127903495','+916127973602','+918079569337','+916127912937','+918912154712','+916571840940','+916127908652','+917979844395','+917378187342','+916127987284','+918701545581','+916127981623','+916127934614','+916127900476','+917195158975','+918847555790','+916120729704','+916127910946','+918779756231','+918917725225','+917979775930','+916127975756','+916127932983','+917261254689','+916578234294','+917931375616','+918217051883','+918079461822','+916127942870','+358501629970','+3584946118698','+358482068382','+3584946987','+358479433','+358494667','+3584946750817','+358503620','+3585078976683','+3584946908890','+35849464727','+3584946890','+358502360888','+358494601897','+358494678','+358501451900','+358494650','+358494641','+35849461880','+3585094893852','+358461132','+3584486773446','+3584946012','+35848414425','+35850597231','+358494621','+3584029417383','+3585017705','+35847875711','+3584835042843','+3584946505','+3585004629','+358494694','+3584946453','+358494691','+3584946354','+3584638022','+358494625598','+358505669','+358494670','+3584946303','+358508204259','+358494659','+3584946422546','+3584049660','+358504585781','+358494605','+358494660','+358494613','+358422270628','+358494633838','+3584946438163','+3584946262','+358446936036','+35849468431','+358509643342','+35850144963','+358434138','+3585084881390','+358423883','+3584946696479','+358485103395','+358504557378','+358456232','+358438008150','+3584549142','+3584946376716','+358500754','+358494629345','+358494686469','+3585097062831','+358494622580','+3584797516060','+3585011937247','+35849464250','+3585007235','+3584946056','+3584488853936','+358494626','+3584946514','+3584946485599','+35849460116','+3584284882','+3585011573','+358494655819','+3584624529','+3584946035557','+3584946821','+358401338','+358494621111','+35850242846','+3584946492397','+3584450864','+35849467442','+358494687','+358494671918','+358494604720','+358494687','+35850428713','+3584946944']

    for i in range(200):
        try:
            name = random_names[i]
            phone = random_phones[i]
            password1 = random.randint(11111, 99999)
            password2 = random.randint(11111, 99999)
            password = f"a{password1}b{password2}"
            obj, created = User.objects.get_or_create(name=name, phone=phone, password=password)
            if created:
                print(f"User {name} has been created.")
            else:
                print(f"{name} with {phone} already exists.")
        except Exception as e:
            print(e)
            
            
def populate_contactlists():
    
    random_phones = ['+5549914182611','+5527901699025','+5522959258463','+5538973682301','+551972644444','+5598984846271','+5527942983900','+554471858755','+554272094776','+5535923794268','+5551918207844','+5511912089855','+5564926461772','+552278208798','+5549996663839','+557476898527','+5528944347675','+5548990297603','+5512969901957','+554178860267','+552475842205','+5569982315288','+5553984429200','+5594993697752','+5554911622442','+559874155422','+5587963045505','+5528957230575','+5524927061531','+556877981840','+556771344450','+5574906801029','+5577910617952','+553270053287','+5587931251344','+552472288796','+5511982766158','+5596943742581','+5584931633728','+5528944511439','+5511982548311','+5541994017346','+553376930170','+552279482677','+5527928261706','+5583945617809','+5592900179363','+5531964407684','+5543918638419','+5545991901697']
    
    random_name = ['IlianaShort','BrandonEsparza','GustavoKeller','AmyaNewton','DillonGarrison','TomasRoberts','SanaaBlack','FelixCarroll','CatalinaPrice','BethanyNeal','TiannaNoble','ThaliaThornton','KarissaOconnor','KeshawnHarris','JaydaFritz','GloriaCasey','MatiasBarr','JimenaBuckley','DelaneyMyers','XzavierKirby','JuniorLawson','DakotaBerger','CassieLove','LyricMcclure','SolomonBenson','HudsonDaniel','AydenLarsen','AbelCooper','ScarletTrevino','SydneeHill','CatalinaMeza','CaraShah','TravisMontoya','WestonPope','SladeTrujillo','BrooksRogers','AaravBoyd','GiulianaAvery','EmersonWare','KaiaCuevas','RoryDunn','MatthiasLiu','KenleyConway','QuinnJennings','CindyLowery','MaddenSchmitt','JusticeMeza','MaliaSellers','KeshawnBrewer','MeghanSmith']
    
    for i in range(50):
        try:
            name = random_name[i]
            phone = random_phones[i]
            if i <= 30:
                if i<10:
                    contact_of_id = 1
                elif i>10 and i<20:
                    contact_of_id = 2
                else:
                    contact_of_id = 3
                obj, created = ContactList.objects.get_or_create(name=name, phone=phone, contact_of_id=contact_of_id)
            else:
                obj, created = ContactList.objects.get_or_create(name=name, phone=phone)
            if created:
                print(f"Contactlist {name} {phone} has been created.")
            else:
                print(f"Contact of {name} with {phone} already exists.")
        except Exception as e:
            print(e)
        
            
populate_contactlists()
populate_users()