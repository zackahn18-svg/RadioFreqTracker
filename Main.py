def run_pccs_interactive_text_only():
    # Pre-Mapped Global Radio Frequency Profile & Coordinate Database
    pccs_global_registry = {
        1665: {
            "station": "Dutch Pirate Radio Net (e.g., Radio Armada / Continental)",
            "region": "Overijssel & Drenthe Countryside, Netherlands",
            "lat": 52.5501, "lon": 6.6214,
            "profile": "Active European mediumwave pirate zone playing Germanic Schlager, polka, and folk music."
        },
        1620: {
            "station": "Northern European Low-Power AM (LPAM) / Pirate Relay",
            "region": "Groningen Border Region, Netherlands / Germany",
            "lat": 53.1235, "lon": 7.0432,
            "profile": "Popular frequency for unauthorized weekend hobbyist music broadcasts using custom tube transmitters."
        },
        3942: {
            "station": "French Navy Tactical Net (Callsigns FUG / FUO)",
            "region": "Brest Naval Base, France",
            "lat": 48.3903, "lon": -4.4860,
            "profile": "Official French military tactical and training channel. Operators occasionally run open transmitter audio tests."
        },
        3955: {
            "station": "Radio Continental / Channel 292 Relay",
            "region": "Rohrbach, Germany",
            "lat": 49.1394, "lon": 8.1278,
            "profile": "High-profile 75m shortwave hotspot broadcasting oldies, Elvis Presley hits, and community music shows."
        },
        3968: {
            "station": "European Shortwave Hobbyist Pirate",
            "region": "Western European Border Zone",
            "lat": 51.4984, "lon": 6.1245,
            "profile": "Monitored broadcasting chill Hawaiian-style instrumental tracks and ambient music on wide audio filters."
        },
        3975: {
            "station": "Shortwave Pirate Relay Station",
            "region": "Central Netherlands",
            "lat": 52.0907, "lon": 5.1214,
            "profile": "Active evening frequency for music relays, hobby testing, and signal reports."
        },
        7345: {
            "station": "China National Radio (CNR 1 - Voice of China)",
            "region": "Shijiazhuang Transmitter Site, China",
            "lat": 38.0422, "lon": 114.5147,
            "profile": "Massive high-power state shortwave transmitter blasting traditional Chinese music and regional news programs worldwide."
        }
    }

    print("=====================================================")
    print("      PYTHON COORDINATE CALCULATION SYSTEM LOADED    ")
    print("      Type 'exit' at any prompt to stop tracking.     ")
    print("=====================================================\n")

    while True:
        # Prompt for frequency input string
        freq_input = input("Enter Frequency Number in kHz (e.g., 1665): ").strip()
        
        # Check for break command exit condition
        if freq_input.lower() == 'exit':
            print("\nShutting down PCCS core engine. Clear skies, Radio Detective!")
            break
            
        # Prompt for modulation format type string
        mode_input = input("Enter Modulation Mode (e.g., AM, USB, LSB): ").strip()
        if mode_input.lower() == 'exit':
            print("\nShutting down PCCS core engine. Clear skies, Radio Detective!")
            break

        # Validate that the user entered a valid integer number
        try:
            target_freq = int(float(freq_input))
        except ValueError:
            print("\nINPUT ERROR: Frequency must be a valid number. Please try again.\n")
            continue

        normalized_mode = mode_input.upper()

        print("\n=== PCCS AUTOMATED TARGET RESOLUTION ===")
        print(f"Captured Input: {target_freq} kHz | Mode: {normalized_mode}")
        print("-------------------------------------------")

        # Execute database validation matching parameters
        if target_freq in pccs_global_registry:
            data = pccs_global_registry[target_freq]
            print(f"POSITION RESOLVED: {data['station']}")
            print(f"Location Profile : {data['region']}")
            print(f"Target Latitude  : {data['lat']:.4f} N")
            print(f"Target Longitude : {data['lon']:.4f} E")
            print(f"Spectrum Notes   : {data['profile']}")
        else:
            print("FREQUENCY NOT PRE-MAPPED - Generating Spectrum Boundaries...")
            if 531 <= target_freq <= 1602:
                print("Expected Region  : Europe / Africa / Asia (ITU Region 1/3)")
                print("Spectrum Notes   : Standard Mediumwave AM broadcast band slot using 9 kHz spacing intervals.")
            elif 1611 <= target_freq <= 1700:
                print("Expected Region  : Western Europe (Highly likely The Netherlands countryside)")
                print("Spectrum Notes   : The Expanded AM Pirate Band. This zone is almost exclusively utilized by Dutch music pirates.")
            elif 3900 <= target_freq <= 4000:
                print("Expected Region  : Continental Europe")
                print("Spectrum Notes   : 75-meter Amateur/Pirate transition band. Frequently active with low-power local operators at night.")
            elif 4000 <= target_freq <= 30000:
                print("Expected Region  : Global / Intercontinental")
                print("Spectrum Notes   : Shortwave Band. Signals at this frequency bounce off the ionosphere and travel thousands of miles.")
            else:
                print("Expected Region  : Outside Target Tracking Bands")
                print("Spectrum Notes   : Verify your entry. Ensure you are tuning into standard Shortwave or Mediumwave blocks.")
                
        print("===========================================\n")

# Run the looping system engine routine
run_pccs_interactive_text_only()
