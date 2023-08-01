class PromptService:
    def times(self):
        return [
            "{{time}}",
            "futuristic",
            "modern",
            "ancient",
            "antique",
            "Retro",
            "old-fashioned",
            "youthful"
        ]

    def types(self):
        return [
            "{{type}}",
            "Abstract Painting",
            "Acrylic Painting",
            "Action Painting",
            "Aestheticism Painting",
            "Anamorphosis Painting",
            "Art Deco Painting",
            "Art nouveau Painting",
            "Ashcan School Painting",
            "Baroque Painting",
            "Body Painting",
            "Canvas Painting",
            "Cartoon Painting",
            "Chalk Painting",
            "Child's Finger Painting",
            "Chinese Painting",
            "Classicism Painting",
            "Collage Painting",
            "Cubism Painting",
            "Dadaism Painting",
            "De Stijl Painting",
            "Der Blaue Painting",
            "Digital Painting",
            "Drip Painting",
            "Enamel Painting",
            "Encaustic Painting",
            "Expressionism Painting",
            "Figurativism Painting",
            "Fingerpainting Painting",
            "Finger Painting",
            "Fresco Secco Painting",
            "Futurism Painting",
            "Genre Painting",
            "Glitter Glue Painting",
            "Gothic Painting",
            "Gouache Painting",
            "History Painting",
            "Hot Wax Painting",
            "Impressionism Painting",
            "Ink Wash Painting",
            "Japanese Painting",
            "Korean Painting",
            "Landscape Painting",
            "Leaf Painting",
            "Marker Painting",
            "Matte Painting",
            "Miniature Painting",
            "Modernism Painting",
            "Mughal Painting",
            "Mural Painting",
            "Oil Painting",
            "Pastel Painting",
            "Pattachitra Painting",
            "Photorealism Painting",
            "Rajasthan Painting",
            "Realism Painting",
            "Reverse Glass Painting",
            "Sand Painting",
            "Speed Painting",
            "Spray Painting",
            "Still Life Painting",
            "Surrealism Painting",
            "Tanjore Painting",
            "Tempera Painting",
            "Velvet Painting",
            "Watercolor Painting",
            "Anime Art",
            "Bedazzled Art Style",
            "Button Art",
            "Chalk Art",
            "Comic Book Art",
            "Conceptual Art",
            "Leather Art Style",
            "Line Art",
            "Marble Art",
            "Pop Art painting",
            "Portrait Art",
            "Sand Art",
            "Street Art",
            "Woven Art",
            "Anime Style",
            "Atari 2600 Style",
            "Bauhaus Style",
            "Coloring Book Style",
            "Constructivism Style",
            "Fauvism Style",
            "Glitter Style",
            "GTAV Style",
            "NES Style",
            "Retro Comic Book Style",
            "SNES Style",
            "Studio Ghibli Style",
            "Woodburning Style",
            "Woodcut Style",
            "Ballpoint Pen Drawing",
            "Blue Ballpoint Pen Drawing",
            "Colored Pencil Drawing",
            "Pencil Drawing",
            "Red Ballpoint Pen Drawing",
            "Comic Book Cover",
            "Comic Book",
            "Comic Book Panel",
            "Colored Pencil Sketch",
            "Pencil Sketch",
            "3D Render",
            "Boxart",
            "Children's Book",
            "Coloring Book",
            "Copper Plate Engraving",
            "Cross-Stitch",
            "Diamond Engraving",
            "Icon",
            "Linocut",
            "Lowpoly",
            "Old Black and White Photograph",
            "Photograph",
            "Pixelart",
            "Pop Up Book",
            "Ring Engraving",
            "Spray Paint",
            "Stained Glass",
            "Sticker",
            "Stone Cut"
        ]

    def art_styles(self):
        return [
            "{{art_style}}"
            "Standard",
            "Japanese anime",
            "Bloodborne",
            "Bauhaus",
            "Concept art",
            "Atompunk",
            "Post modern",
            "Renaissance",
            "Art Nouveau",
            "Art Deco",
            "Flowerpunk",
            "Surreal",
            "Dieselpunk",
            "Solarpunk",
            "Pixar movie style",
            "Cyber punk style",
            "Steam punk",
            "Grunge",
            "Industrialpunk",
        ]

    def artists(self):
        return [
            "{{artist}}",
            "Agnes Lawrence Pelton",
            "Akihito Yoshida",
            "Alex Grey",
            "Alexander Jansson",
            "Alphonse Mucha",
            "Andreas Rocha",
            "Andy Warhol",
            "Artgerm",
            "Asaf Hanuka",
            "Asher Brown Durand",
            "Aubrey Beardsley",
            "Banksy",
            "Beeple",
            "Ben Enwonwu",
            "Bob Eggleton",
            "Caravaggio Michelangelo Merisi",
            "Caspar David Friedrich",
            "Chris Foss",
            "Claude Monet",
            "Dan Mumford",
            "David Mann",
            "Diego Velázquez",
            "Disney Animation Studios",
            "Édouard Manet",
            "Esao Andrews",
            "Frida Kahlo",
            "Gediminas Pranckevicius",
            "Georgia O'Keeffe",
            "Greg Rutkowski",
            "Gustave Doré",
            "Gustave Klimt",
            "H.R. Giger",
            "Hayao Miyazaki",
            "Henri Matisse",
            "HP Lovecraft",
            "Ivan Shishkin",
            "Jack Kirby",
            "Jackson Pollock",
            "James Jean",
            "Jean-Baptiste Monge",
            "Jim Burns",
            "Johannes Vermeer",
            "John William Waterhouse",
            "Katsushika Hokusai",
            "Kim Tschang Yeul",
            "Ko Young Hoon",
            "Leonardo da Vinci",
            "Lisa Frank",
            "M.C. Escher",
            "Mahmoud Saïd",
            "Makoto Shinkai",
            "Marc Simonetti",
            "Mark Brooks",
            "Michelangelo",
            "Pablo Picasso",
            "Paul Klee",
            "Peter Mohrbacher",
            "Pierre-Auguste Renoir",
            "Pixar Animation Studios",
            "Rembrandt",
            "Renato Mucillo",
            "Richard Dadd",
            "Rossdraws",
            "Salvador Dalí",
            "Sam Does Arts",
            "Sandro Botticelli",
            "Ted Nasmith",
            "Ten Hundred",
            "Thomas Kinkade",
            "Tivadar Csontváry Kosztka",
            "Victo Ngai",
            "Vincent Di Fate",
            "Vincent van Gogh",
            "Wes Anderson",
            "wlop",
            "Yoshitaka Amano"
        ]

    def realisms(self):
        return [
            "{{realism}}",
            "Photorealistic",
            "Ultra photoreal",
            "Ultra detailed",
            "Intricate details",
            "Atmospheric",
            "Hyperrealistic",
            "Sharp focus",
            "Multiverse",
            "Realistic CGI",
            "Ambient occlusion",
        ]

    def rendering_engines(self):
        return ["{{rendering_engine}}", "Unreal engine", "Ray tracing", "Octane render", "V-ray"]

    def lightning_angles(self):
        return [
            "{{lightning_angle}}",
            "Top light",
            "Back light",
            "Front light",
            "Light from right",
            "Light from left",
        ]

    def lightning_styles(self):
        return [
            "{{lightning_style}}",
            "Volumetric",
            "Cinematic",
            "Uplight",
            "Softbox",
            "Flash",
            "Glowing",
            "Fairy lights",
            "Multicolor",
            "Rim lighting",
            "Soft lighting",
            "Fantastic backlight",
            "Internal glow",
            "Iridescent",
            "Rainbow",
        ]

    def camera_positions(self):
        return [
            "{{camera_position}}",
            "High camera",
            "Insect eye",
            "Low camera",
            "Wide-Angle Shot",
            "Ultra-Wide-Angle Shot",
            "Satellite View",
            "Eye-Level Shot",
            "Far-Shot Angle",
            "Medium-Shot Angle",
            "Ground-Shot Angle",
            "Low-Angle Shot",
            "Full-Shot Angle",
            "Full-Body Shot",
            "Glamour Shot",
            "Cinematic Still Shot",
            "Birds-eye",
        ]

    def cameras(self):
        return ["{{camera}}", "Nikon", "Canon", "Sony alpha", "Leica M", "Leica"]

    def styles(self):
        return [
            "{{style}}",
            "Macro",
            "Long exposure",
            "Fisheye",
            "Polaroid",
            "Kodachrome",
            "Golden hour",
            "Infrared",
            "Early wet plate",
        ]

    def compositions(self):
        return [
            "{{composition}}",
            "Symmetrical",
            "Golden ratio",
            "Centered",
            "Triangular composition",
            "Asymetric",
        ]

    def isos(self):
        return [
            "ISO50",
            "ISO100",
            "ISO200",
            "ISO400",
            "ISO800",
            "ISO1600",
            "ISO3200",
            "ISO6400",
            "ISO12800",
        ]

    def resolutions(self):
        return [
            "{{resolution}}",
            "8k",
            "HD",
            "Full HD",
        ]

    def generate(self, args):
        separator = ", "
        output = ""
        if args.type != None:
            output += args.type + " of "
        output += separator.join(args.description)
        if args.background_color != None:
            output += " with background " + args.background_color
        if args.art_style != None and len(args.art_style) > 0:
            output += separator + separator.join(args.art_style)
        if args.artist != None and len(args.artist) > 0:
            output += separator + "by " + separator.join(args.artist)
        if args.realism != None and len(args.realism) > 0:
            output += separator + separator.join(args.realism)
        if args.rendering_engine != None and len(args.rendering_engine) > 0:
            output += separator + separator.join(args.rendering_engine)
        if args.lightning_angle != None and len(args.lightning_angle) > 0:
            output += separator + separator.join(args.lightning_angle)
        if args.lightning_style != None and len(args.lightning_style) > 0:
            output += separator + separator.join(args.lightning_style)
        if args.camera_position != None and len(args.camera_position) > 0:
            output += separator + separator.join(args.camera_position)
        if args.camera != None and len(args.camera) > 0:
            output += separator + separator.join(args.camera)
        if args.style != None and len(args.style) > 0:
            output += separator + separator.join(args.style)
        if args.composition != None and len(args.composition) > 0:
            output += separator + separator.join(args.composition)
        if args.iso != None:
            output += separator + args.iso
        if args.resolution != None and len(args.resolution) > 0:
            output += separator + separator.join(args.resolution)
        return output
