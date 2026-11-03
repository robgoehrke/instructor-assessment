# locations.py

LOCATIONS = sorted([
    # --- UNITED STATES ---
    # Alabama
    "AL - Birmingham", "AL - Huntsville", "AL - Mobile",
    # Arkansas
    "AR - Bentonville", "AR - Fayetteville", "AR - Little Rock",
    # Arizona
    "AZ - Ahwatukee (Chandler)", "AZ - Arcadia (Phoenix)", "AZ - Gilbert", 
    "AZ - Goodyear / Litchfield Park", "AZ - North Scottsdale", "AZ - Peoria", 
    "AZ - Queen Creek", "AZ - Scottsdale", "AZ - Tempe", "AZ - Tucson",
    # California
    "CA - Anaheim", "CA - Burbank", "CA - Carlsbad", "CA - Carmichael", 
    "CA - Castro Valley", "CA - Cerritos", "CA - Chula Vista (Otay Ranch)", 
    "CA - Claremont", "CA - Costa Mesa", "CA - Del Mar", "CA - Eagle Rock", 
    "CA - Elk Grove", "CA - Encinitas", "CA - Fairfax District LA", "CA - Folsom", 
    "CA - Fremont", "CA - Huntington Beach", "CA - Irvine", "CA - Laguna Niguel", 
    "CA - Long Beach", "CA - Los Gatos", "CA - Mill Valley", "CA - Mission Viejo", 
    "CA - Mountain View", "CA - Newport Beach", "CA - Oakland", "CA - Oceanside", 
    "CA - Orange", "CA - Pasadena", "CA - Petaluma", "CA - Pleasanton", 
    "CA - Rancho Cucamonga", "CA - Rancho Santa Margarita", 
    "CA - Redondo Beach (South Bay L.A.)", "CA - Redwood City", 
    "CA - Rolling Hills Estates (Palos Verdes)", "CA - Roseville", 
    "CA - Sacramento (Land Park)", "CA - San Carlos", "CA - San Diego", 
    "CA - San Francisco", "CA - San Jose", "CA - San Mateo", "CA - San Rafael", 
    "CA - Santa Ana", "CA - Santa Barbara", "CA - Santa Clarita", 
    "CA - Santa Monica", "CA - Santa Rosa", "CA - Scripps Ranch", 
    "CA - Silver Lake", "CA - Sunnyvale", "CA - Temecula", "CA - Thousand Oaks", 
    "CA - Torrance", "CA - Tustin", "CA - Vacaville", "CA - Venice", 
    "CA - Ventura", "CA - Walnut Creek", "CA - West Hills (Woodland Hills)", 
    "CA - West LA",
    # Colorado
    "CO - Aurora", "CO - Boulder", "CO - Broomfield", "CO - Centennial", 
    "CO - Colorado Springs", "CO - Denver", "CO - Denver Highlands", 
    "CO - Fort Collins", "CO - Golden / Lakewood", "CO - Highlands Ranch", 
    "CO - Littleton", "CO - Longmont", "CO - Parker",
    # Connecticut
    "CO - Fairfield", "CT - Greenwich", "CT - Madison", "CT - New Canaan", 
    "CT - North Haven", "CT - Ridgefield", "CT - Stamford", "CT - West Hartford", 
    "CT - Westport",
    # Delaware / DC
    "DC - Washington DC / Cleveland Park", "DE - Hockessin", "DE - Middletown",
    # Florida
    "FL - Boca Raton", "FL - Bradenton (Lakewood Ranch)", "FL - Brandon", 
    "FL - Clearwater", "FL - Clermont", "FL - Coconut Grove", "FL - Coral Gables", 
    "FL - Coral Springs", "FL - Davie (West Broward)", "FL - Delray Beach", 
    "FL - Doral", "FL - Fort Lauderdale", "FL - Fort Myers", "FL - Gainesville", 
    "FL - Hollywood", "FL - Jacksonville (Mandarin)", "FL - Jupiter", 
    "FL - Lake Mary", "FL - Lake Worth (South Palm Beach)", "FL - Lakeland", 
    "FL - Lutz", "FL - Miami", "FL - Naples", "FL - North Miami", 
    "FL - North Palm Beach", "FL - Orlando", "FL - Oviedo", "FL - Palm Beach Gardens", 
    "FL - Palm City", "FL - Palmetto Bay", "FL - Pompano Beach", "FL - Sarasota", 
    "FL - South Miami", "FL - St. Petersburg", "FL - Tallahassee", "FL - Tampa", 
    "FL - Wellington", "FL - West Palm Beach", "FL - Winter Park",
    # Georgia
    "GA - Alpharetta", "GA - Atlanta (Buckhead)", "GA - Buford", "GA - Decatur", 
    "GA - Dunwoody", "GA - Holly Springs (Woodstock)", "GA - Johns Creek", 
    "GA - Kennesaw (West Cobb)", "GA - Lawrenceville", "GA - Marietta (East Cobb)", 
    "GA - Midtown Atlanta", "GA - Peachtree City", "GA - Roswell", 
    "GA - Sandy Springs", "GA - Smyrna", "GA - Suwanee",
    # Iowa / Idaho
    "IA - Ankeny", "IA - Cedar Rapids / Marion", "IA - Des Moines", 
    "IA - West Des Moines", "ID - Boise", "ID - Meridian",
    # Illinois
    "IL - Andersonville", "IL - Arlington Heights", "IL - Barrington", 
    "IL - Chicago", "IL - Chicago West", "IL - Elmhurst", "IL - Evanston", 
    "IL - Frankfort", "IL - Geneva", "IL - Glen Ellyn", "IL - Glenbrook (Northbrook)", 
    "IL - Hinsdale", "IL - Lake Zurich", "IL - Lemont", "IL - Libertyville", 
    "IL - Mokena", "IL - Naperville", "IL - Oak Park", "IL - Orland Park", 
    "IL - Oswego", "IL - Park Ridge", "IL - Plainfield", "IL - Saint Charles", 
    "IL - Schaumburg", "IL - Shorewood", "IL - Vernon Hills", "IL - Wheaton",
    # Indiana
    "IN - Bloomington", "IN - Carmel", "IN - Castleton", "IN - Fishers", 
    "IN - Fort Wayne", "IN - Greenwood", "IN - Indianapolis", "IN - Noblesville", 
    "IN - South Bend", "IN - Westfield", "IN - Zionsville",
    # Kansas / Kentucky
    "KS - Overland Park", "KS - Shawnee", "KS - Wichita", 
    "KY - Florence (Northern Kentucky)", "KY - Lexington", "KY - Louisville (East)", 
    "KY - Louisville (St. Matthews)",
    # Louisiana
    "LA - Baton Rouge", "LA - Lafayette", "LA - Mandeville (Northshore)", 
    "LA - Metairie / New Orleans", "LA - Shreveport",
    # Massachusetts
    "MA - Attleboro", "MA - Boston", "MA - Brookline", "MA - Burlington", 
    "MA - Cambridge", "MA - Dedham", "MA - Franklin", "MA - Lynnfield", 
    "MA - Medford", "MA - Natick", "MA - Newton", "MA - Northborough", 
    "MA - Norwood / Walpole", "MA - Peabody", "MA - Plymouth", "MA - Quincy", 
    "MA - Seekonk", "MA - Somerville", "MA - Wakefield", "MA - Watertown", 
    "MA - Wellesley", "MA - Westborough", "MA - Weymouth",
    # Maryland
    "MD - Annapolis (Arnold)", "MD - Baltimore", "MD - Bethesda", "MD - Clarksburg", 
    "MD - Columbia", "MD - Frederick", "MD - Gaithersburg", "MD - Gambrills", 
    "MD - Germantown", "MD - Pikesville", "MD - Rockville", "MD - Silver Spring", 
    "MD - Towson",
    # Michigan
    "MI - Ann Arbor", "MI - Birmingham", "MI - Brighton", "MI - Canton", 
    "MI - Detroit", "MI - East Lansing (Okemos)", "MI - Farmington", 
    "MI - Grand Rapids", "MI - Grosse Pointe", "MI - Northville", 
    "MI - Rochester", "MI - Royal Oak", "MI - Troy", "MI - West Bloomfield",
    # Minnesota
    "MN - Blaine", "MN - Burnsville", "MN - Chanhassen", "MN - Coon Rapids", 
    "MN - Eagan", "MN - Eden Prairie", "MN - Edina", "MN - Maple Grove", 
    "MN - Medina (Plymouth)", "MN - Minnetonka", "MN - St. Paul", "MN - Woodbury",
    # Missouri
    "MO - Ballwin", "MO - Chesterfield", "MO - Columbia", "MO - Kansas City", 
    "MO - Kirkwood", "MO - Lee's Summit", "MO - Parkville (Kansas City)", 
    "MO - Springfield", "MO - St. Charles", "MO - St. Louis", "MO - St. Peters", 
    "MO - Webster Groves",
    # Mississippi / Montana
    "MS - Jackson", "MS - Southaven", "MT - Bozeman", "MT - Missoula",
    # North Carolina
    "NC - Apex", "NC - Asheville", "NC - Cary", "NC - Chapel Hill", 
    "NC - Charlotte", "NC - Cornelius / Lake Norman", "NC - Durham", 
    "NC - Greensboro", "NC - Holly Springs", "NC - Huntersville", 
    "NC - Matthews", "NC - North Charlotte", "NC - Raleigh", 
    "NC - Wake Forest", "NC - Waxhaw (Wesley Chapel)", "NC - Wilmington", 
    "NC - Winston-Salem",
    # Nebraska / New Hampshire
    "NE - Omaha", "NH - Manchester", "NH - Nashua", "NH - Portsmouth",
    # New Jersey
    "NJ - Aberdeen", "NJ - Berkeley Heights", "NJ - Chatham", "NJ - Cherry Hill", 
    "NJ - Clark Township", "NJ - Closter", "NJ - Cresskill", "NJ - Denville", 
    "NJ - Deptford Township", "NJ - East Brunswick", "NJ - Englewood", 
    "NJ - Fair Lawn", "NJ - Flemington", "NJ - Freehold", "NJ - Glen Rock", 
    "NJ - Hackensack", "NJ - Hillsborough", "NJ - Hoboken", "NJ - Livingston", 
    "NJ - Mahwah", "NJ - Marlboro (Morganville)", "NJ - Matawan", "NJ - Maywood", 
    "NJ - Medford", "NJ - Metuchen", "NJ - Millburn", "NJ - Montclair", 
    "NJ - Montvale", "NJ - Morristown", "NJ - Nutley", "NJ - Paramus", 
    "NJ - Parsippany-Troy Hills", "NJ - Princeton (Lawrence)", "NJ - Ramsey", 
    "NJ - Randolph", "NJ - Red Bank", "NJ - Ridgewood", "NJ - Roselle Park", 
    "NJ - Saddle Brook", "NJ - Scotch Plains", "NJ - Shrewsbury", 
    "NJ - Somerville", "NJ - South Orange", "NJ - South Plainfield", 
    "NJ - Summit", "NJ - Tenafly", "NJ - Toms River", "NJ - Waldwick", 
    "NJ - Wayne", "NJ - Westfield", "NJ - Woodcliff Lake",
    # New Mexico / Nevada
    "NM - Albuquerque", "NM - Santa Fe", "NV - Henderson (Green Valley)", 
    "NV - Las Vegas Summerlin", "NV - Las Vegas West", "NV - NW Las Vegas", 
    "NV - Reno", "NV - Sparks",
    # New York
    "NY - Albany", "NY - Astoria (Queens)", "NY - Bayside", "NY - Bay Ridge (Brooklyn)", 
    "NY - Bedford", "NY - Bellmore", "NY - Bronx", "NY - Brooklyn", 
    "NY - Buffalo (East Amherst)", "NY - Commack", "NY - East Meadow", 
    "NY - Farmingdale", "NY - Fayetteville (Syracuse)", "NY - Fleetwood", 
    "NY - Garden City", "NY - Glen Cove", "NY - Huntington", "NY - Larchmont", 
    "NY - Mamaroneck", "NY - Manhattan (Upper East Side)", "NY - Manhattan (Upper West Side)", 
    "NY - Melville", "NY - Mount Kisco", "NY - New City (Rockland)", 
    "NY - New York (Midtown)", "NY - Oyster Bay (Syosset)", "NY - Port Jefferson", 
    "NY - Port Washington", "NY - Queens", "NY - Riverhead", "NY - Rochester (Victor)", 
    "NY - Rockville Centre", "NY - Roslyn", "NY - Rye", "NY - Scarsdale", 
    "NY - Sayville", "NY - Smithtown", "NY - Southampton", "NY - Staten Island", 
    "NY - Syracuse", "NY - Tarrytown", "NY - Wappingers Falls", "NY - White Plains", 
    "NY - Williamsburg (Brooklyn)", "NY - Yorktown Heights",
    # Ohio
    "OH - Akron", "OH - Beavercreek", "OH - Centerville", "OH - Cincinnati", 
    "OH - Cleveland (Lakewood)", "OH - Cleveland West (Westlake)", "OH - Columbus (Clintonville)", 
    "OH - Columbus (Gahanna)", "OH - Dayton", "OH - Dublin", "OH - Highland Heights", 
    "OH - Mason", "OH - Medina", "OH - Perrysburg", "OH - Powell", 
    "OH - Strongsville", "OH - Toledo", "OH - Westerville",
    # Oklahoma
    "OK - Broken Arrow", "OK - Edmond", "OK - Jenks", "OK - Norman", 
    "OK - Oklahoma City", "OK - Tulsa",
    # Oregon
    "OR - Beaverton", "OR - Bend", "OR - Eugene", "OR - Lake Oswego (Tigard)", 
    "OR - Portland", "OR - Salem",
    # Pennsylvania
    "PA - Allentown", "PA - Berwyn (Main Line)", "PA - Bethlehem", 
    "PA - Blue Bell", "PA - Conshohocken", "PA - Downingtown", "PA - Doylestown", 
    "PA - Easton", "PA - Exton", "PA - Fort Washington", "PA - Glen Mills", 
    "PA - Harrisburg", "PA - King of Prussia", "PA - Lancaster", "PA - Media (Delco)", 
    "PA - Newtown", "PA - Philadelphia (Center City)", "PA - Philadelphia (Manayunk)", 
    "PA - Pittsburgh (North Hills)", "PA - Pittsburgh (South Hills)", "PA - Plymouth Meeting", 
    "PA - Royersford", "PA - Wayne", "PA - West Chester", "PA - Wexford", "PA - York",
    # Rhode Island / South Carolina
    "RI - Cranston", "RI - East Greenwich", "RI - Providence", 
    "SC - Charleston", "SC - Columbia", "SC - Fort Mill", "SC - Greenville (Simpsonville)", 
    "SC - Mount Pleasant", "SC - Myrtle Beach", "SC - Rock Hill",
    # Tennessee
    "TN - Chattanooga", "TN - Clarksville", "TN - Franklin", "TN - Germantown", 
    "TN - Hendersonville", "TN - Knoxville", "TN - Memphis", "TN - Memphis (Wolfchase)", 
    "TN - Mt. Juliet", "TN - Murfreesboro", "TN - Nashville",
    # Texas
    "TX - Allen", "TX - Amarillo", "TX - Arlington", "TX - Austin", 
    "TX - Austin (Round Rock)", "TX - Austin (Westlake)", "TX - Bellaire", 
    "TX - Bryan / College Station", "TX - Cedar Park", "TX - Champion Forest", 
    "TX - Clear Lake", "TX - Conroe", "TX - Coppell", "TX - Cypress", 
    "TX - Dallas", "TX - Denton", "TX - Flower Mound", "TX - Fort Worth", 
    "TX - Friendswood", "TX - Frisco", "TX - Garland", "TX - Georgetown", 
    "TX - Grapevine", "TX - Houston (Heights)", "TX - Houston (Memorial)", 
    "TX - Houston (Midtown)", "TX - Houston (West)", "TX - Katy", 
    "TX - Keller (Southlake)", "TX - Kingwood", "TX - League City", 
    "TX - Lewisville", "TX - Lubbock", "TX - Mansfield", "TX - McKinney", 
    "TX - Pearland", "TX - Plano", "TX - Richardson", "TX - Rockwall", 
    "TX - Saginaw", "TX - San Antonio", "TX - San Antonio (Stone Oak)", 
    "TX - Southlake", "TX - Spring", "TX - Sugar Land", "TX - Summer Creek", 
    "TX - The Woodlands", "TX - Tyler", "TX - Waco", "TX - Webster", 
    "TX - West University Place",
    # Utah
    "UT - Draper", "UT - Lehi", "UT - Orem", "UT - Park City", 
    "UT - Salt Lake City", "UT - Sandy", "UT - South Jordan", "UT - St. George",
    # Virginia
    "VA - Alexandria", "VA - Arlington", "VA - Ashburn", "VA - Charlottesville", 
    "VA - Chesapeake", "VA - Fairfax", "VA - Falls Church", "VA - Fredericksburg", 
    "VA - Gainesville", "VA - Haymarket", "VA - Leesburg", "VA - McLean", 
    "VA - Midlothian", "VA - Newport News", "VA - Norfolk", "VA - Reston", 
    "VA - Richmond", "VA - Roanoke", "VA - Springfield", "VA - Virginia Beach", 
    "VA - Williamsburg", "VA - Woodbridge",
    # Washington
    "WA - Bellevue", "WA - Bellingham", "WA - Bothell", "WA - Edmonds", 
    "WA - Federal Way", "WA - Issaquah", "WA - Kirkland", "WA - Lynnwood", 
    "WA - Olympia", "WA - Redmond", "WA - Renton", "WA - Seattle", 
    "WA - Spokane", "WA - Tacoma", "WA - Vancouver",
    # Wisconsin
    "WI - Appleton", "WI - Brookfield", "WI - Green Bay", "WI - Madison", 
    "WI - Milwaukee", "WI - Shorewood", "WI - Waukesha",

    # --- CANADA ---
    "AB - Calgary", "AB - Calgary Douglasdale", "AB - Edmonton",
    "BC - Abbotsford", "BC - Burnaby", "BC - Coquitlam", "BC - Langley", 
    "BC - North Vancouver", "BC - Surrey", "BC - Vancouver", "BC - Victoria", 
    "BC - White Rock",
    "ON - Aurora", "ON - Burlington", "ON - Guelph", "ON - Hamilton", 
    "ON - Kingston", "ON - Kitchener-Waterloo", "ON - London", "ON - Markham", 
    "ON - Mississauga", "ON - Newmarket", "ON - Oakville", "ON - Orleans", 
    "ON - Ottawa", "ON - Richmond Hill", "ON - Toronto (Central)", 
    "ON - Toronto (East)", "ON - Toronto (West)", "ON - Vaughan", "ON - Whitby", 
    "QC - Montreal (West Island)", "QC - Montreal (Downtown)",

    # --- INTERNATIONAL ---
    # Australia
    "Australia - Bella Vista", "Australia - Campbelltown", "Australia - Dee Why", 
    "Australia - Hawthorn", "Australia - Macarthur", "Australia - Marrickville", 
    "Australia - Ringwood", "Australia - St Kilda",
    # Brazil
    "Brazil - Moema (São Paulo)", "Brazil - Pinheiros (São Paulo)", 
    "Brazil - Jardins (São Paulo)", "Brazil - Curitiba", "Brazil - Porto Alegre", 
    "Brazil - Rio de Janeiro (Ipanema)", "Brazil - Campinas", "Brazil - Belo Horizonte",
    # Chile & Colombia
    "Chile - Santiago (Las Condes)", "Chile - Santiago (Lo Barnechea)", 
    "Chile - Santiago (La Dehesa)", "Chile - Santiago (Vitacura)", 
    "Chile - Viña del Mar", "Colombia - Bogotá (Chicó)", "Colombia - Bogotá (Usaquén)", 
    "Colombia - Medellín (El Poblado)",
    # Mexico
    "Mexico - Guadalajara", "Mexico - Mexico City (Polanco)", 
    "Mexico - Mexico City (Pedregal)", "Mexico - Mexico City (Satélite)", 
    "Mexico - Monterrey", "Mexico - Puebla", "Mexico - Querétaro", 
    "Mexico - San Pedro Garza García",
    # Europe
    "Germany - München", "Ireland - Dublin (Blackrock)", 
    "Portugal - Faro", "Portugal - Lisboa", "Portugal - Oeiras", "Portugal - Portimão",
    "Spain - Barcelona", "Spain - Madrid (Alcobendas)", "Spain - Madrid (Chamberí)",
    "UK - London (Twickenham)", "UK - London (Dulwich)", "UK - London (Battersea)",
    # Latin America / Asia-Pacific
    "Peru - Lima (Miraflores)", "Peru - Lima (San Isidro)", 
    "Philippines - Manila (Greenhills)", "Philippines - Manila (Alabang)",
    "Paraguay - Asunción", "South Africa - Johannesburg", "South Africa - Cape Town"
])
