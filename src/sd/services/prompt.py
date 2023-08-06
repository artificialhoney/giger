import io


class PromptService:
    def compel_styles(self):
        return [
            "subtle",
            "full"
        ]

    def times(self):
        return [
            "Ancient",
            "Antique",
            "Futuristic",
            "Modern",
            "Old-fashioned",
            "Retro",
            "Youthful"
            "{{time}}",
        ]

    def types(self):
        return [
            "3D Render",
            "Abstract Painting",
            "Acrylic Painting",
            "Action Painting",
            "Aestheticism Painting",
            "Anamorphosis Painting",
            "Anime Art",
            "Anime Style",
            "Art Deco Painting",
            "Art nouveau Painting",
            "Ashcan School Painting",
            "Atari 2600 Style",
            "Ballpoint Pen Drawing",
            "Baroque Painting",
            "Bauhaus Style",
            "Bedazzled Art Style",
            "Blue Ballpoint Pen Drawing",
            "Body Painting",
            "Boxart",
            "Button Art",
            "Canvas Painting",
            "Cartoon Painting",
            "Chalk Art",
            "Chalk Painting",
            "Child's Finger Painting",
            "Children's Book",
            "Chinese Painting",
            "Classicism Painting",
            "Collage Painting",
            "Colored Pencil Drawing",
            "Colored Pencil Sketch",
            "Coloring Book Style",
            "Coloring Book",
            "Comic Book Art",
            "Comic Book Cover",
            "Comic Book Panel",
            "Comic Book",
            "Conceptual Art",
            "Constructivism Style",
            "Copper Plate Engraving",
            "Cross-Stitch",
            "Cubism Painting",
            "Dadaism Painting",
            "De Stijl Painting",
            "Der Blaue Painting",
            "Diamond Engraving",
            "Digital Painting",
            "Drip Painting",
            "Enamel Painting",
            "Encaustic Painting",
            "Expressionism Painting",
            "Fauvism Style",
            "Figurativism Painting",
            "Finger Painting",
            "Fingerpainting Painting",
            "Fresco Secco Painting",
            "Futurism Painting",
            "GTAV Style",
            "Genre Painting",
            "Glitter Glue Painting",
            "Glitter Style",
            "Gothic Painting",
            "Gouache Painting",
            "History Painting",
            "Hot Wax Painting",
            "Icon",
            "Impressionism Painting",
            "Ink Wash Painting",
            "Japanese Painting",
            "Korean Painting",
            "Landscape Painting",
            "Leaf Painting",
            "Leather Art Style",
            "Line Art",
            "Linocut",
            "Lowpoly",
            "Marble Art",
            "Marker Painting",
            "Matte Painting",
            "Miniature Painting",
            "Modernism Painting",
            "Mughal Painting",
            "Mural Painting",
            "NES Style",
            "Oil Painting",
            "Old Black and White Photograph",
            "Pastel Painting",
            "Pattachitra Painting",
            "Pencil Drawing",
            "Pencil Sketch",
            "Photograph",
            "Photorealism Painting",
            "Pixelart",
            "Pop Art painting",
            "Pop Up Book",
            "Portrait Art",
            "Rajasthan Painting",
            "Realism Painting",
            "Red Ballpoint Pen Drawing",
            "Retro Comic Book Style",
            "Reverse Glass Painting",
            "Ring Engraving",
            "SNES Style",
            "Sand Art",
            "Sand Painting",
            "Speed Painting",
            "Spray Paint",
            "Spray Painting",
            "Stained Glass",
            "Sticker",
            "Still Life Painting",
            "Stone Cut"
            "Street Art",
            "Studio Ghibli Style",
            "Surrealism Painting",
            "Tanjore Painting",
            "Tempera Painting",
            "Velvet Painting",
            "Watercolor Painting",
            "Woodburning Style",
            "Woodcut Style",
            "Woven Art",
            "{{type}}",
        ]

    def art_styles(self):
        return [
            "Art Deco",
            "Art Nouveau",
            "Atompunk",
            "Bauhaus",
            "Bloodborne",
            "Concept Art",
            "Cyber Punk Style",
            "Dieselpunk",
            "Flowerpunk",
            "Grunge",
            "Industrialpunk",
            "Japanese Anime",
            "Pixar Movie Style",
            "Post Modern",
            "Renaissance",
            "Solarpunk",
            "Standard",
            "Steam Punk",
            "Surreal",
            "{{art_style}}"

        ]

    def artists(self):
        return [
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
            "Esao Andrews",
            "Frank Miller",
            "Frida Kahlo",
            "Gediminas Pranckevicius",
            "Georgia O'Keeffe",
            "Greg Rutkowski",
            "Gustave Doré",
            "Gustave Klimt",
            "H.R. Giger",
            "HP Lovecraft",
            "Hayao Miyazaki",
            "Henri Matisse",
            "Hieronymus Bosch",
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
            "William Blake",
            "Yoshitaka Amano"
            "Édouard Manet",
            "{{artist}}",
        ]

    def realisms(self):
        return [
            "Ambient Occlusion",
            "Atmospheric",
            "Hyperrealistic",
            "Intricate Details",
            "Multiverse",
            "Photorealistic",
            "Realistic CGI",
            "Sharp Focus",
            "Ultra Detailed",
            "Ultra Photoreal",
            "{{realism}}",
        ]

    def rendering_engines(self):
        return [
            "Octane Render",
            "Ray Tracing",
            "Unreal Engine",
            "V-Ray"
            "{{rendering_engine}}",
        ]

    def lightning_angles(self):
        return [
            "Back Light",
            "Front Light",
            "Light From Left",
            "Light From Right",
            "Top Light",
            "{{lightning_angle}}",
        ]

    def lightning_styles(self):
        return [
            "Cinematic",
            "Fairy Lights",
            "Fantastic Backlight",
            "Flash",
            "Glowing",
            "Internal Glow",
            "Iridescent",
            "Multicolor",
            "Rainbow",
            "Rim Lighting",
            "Soft Lighting",
            "Softbox",
            "Uplight",
            "Volumetric",
            "{{lightning_style}}",
        ]

    def camera_positions(self):
        return [
            "Birds-eye",
            "Cinematic Still Shot",
            "Eye-Level Shot",
            "Far-Shot Angle",
            "Full-Body Shot",
            "Full-Shot Angle",
            "Glamour Shot",
            "Ground-Shot Angle",
            "High Camera",
            "Insect Eye",
            "Low camera",
            "Low-Angle Shot",
            "Medium-Shot Angle",
            "Satellite View",
            "Ultra-Wide-Angle Shot",
            "Wide-Angle Shot",
            "{{camera_position}}",
        ]

    def cameras(self):
        return [
            "Canon",
            "Leica M",
            "Leica"
            "Nikon",
            "Sony alpha",
            "{{camera}}",
        ]

    def styles(self):
        return [
            "Early Wet Plate",
            "Fisheye",
            "Golden hour",
            "Infrared",
            "Kodachrome",
            "Long Exposure",
            "Macro",
            "Polaroid",
            "{{style}}",
        ]

    def compositions(self):
        return [
            "Asymetric",
            "Centered",
            "Golden Ratio",
            "Symmetrical",
            "Triangular Composition",
            "{{composition}}",
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

        context = []
        description = []
        style = []
        image = []
        lora = []

        if args.time != None:
            context.append(args.time)
        if args.type != None:
            context.append(args.type)

        if isinstance(args.description, io.TextIOWrapper):
            description = args.description.read()
        else:
            description = args.description
        description = [x.strip() for x in description.split(',')]

        if args.background_color != None:
            style.append("with background " + args.background_color)
        if args.art_style != None and len(args.art_style) > 0:
            style.append(separator.join(args.art_style))
        if args.artist != None and len(args.artist) > 0:
            style.append("by " + separator.join(args.artist))

        if args.realism != None and len(args.realism) > 0:
            image.append(separator.join(args.realism))
        if args.rendering_engine != None and len(args.rendering_engine) > 0:
            image.append(separator.join(args.rendering_engine))
        if args.lightning_angle != None and len(args.lightning_angle) > 0:
            image.append(separator.join(args.lightning_angle))
        if args.lightning_style != None and len(args.lightning_style) > 0:
            image.append(separator.join(args.lightning_style))
        if args.camera_position != None and len(args.camera_position) > 0:
            image.append(separator.join(args.camera_position))
        if args.camera != None and len(args.camera) > 0:
            image.append(separator.join(args.camera))
        if args.style != None and len(args.style) > 0:
            image.append(separator.join(args.style))
        if args.composition != None and len(args.composition) > 0:
            image.append(separator.join(args.composition))
        if args.iso != None:
            image.append(args.iso)
        if args.resolution != None and len(args.resolution) > 0:
            image.append(separator.join(args.resolution))

        if args.lora != None:
            lora = ["<lora:" + x + ">" for x in args.lora]

        if args.compel_style == "subtle":
            segments = []
            lead = context + description + style
            if len(lead) > 0:
                segments.append("\"" + separator.join(lead) + "\"")
            if len(image) > 0:
                segments.append("\"" + separator.join(image) + "\"")
            if len(lora) > 0:
                segments.append("\"" + separator.join(lora) + "\"")
            return "({0}).and()".format(separator.join(segments))
        if args.compel_style == "full":
            segments = []
            if len(description) > 0:
                segments.append(separator.join(["\"" + x + "\"" for x in description]))
            if len(context) > 0:
                segments.append("\"" + " ".join(context) + "\"")
            if len(style) > 0:
                segments.append("\"" + separator.join(style) + "\"")
            if len(image) > 0:
                segments.append("\"" + separator.join(image) + "\"")
            if len(lora) > 0:
                segments.append("\"" + separator.join(lora) + "\"")
            return "({0}).and()".format(separator.join(segments))
        else:
            return separator.join(context + description + style + image + lora)
