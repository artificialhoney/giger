import io


class PromptService:
    def compel_styles():
        return ["subtle", "full"]

    def times():
        return [
            "Ancient",
            "Antique",
            "Futuristic",
            "Modern",
            "Old-fashioned",
            "Retro",
            "Youthful",
            "{{time}}",
        ]

    def types():
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
            "Stone Cut",
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

    def art_styles():
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
            "{{art_style}}",
        ]

    def artists():
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
            "Rosgigerraws",
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
            "Yoshitaka Amano",
            "Édouard Manet",
            "{{artist}}",
        ]

    def realisms():
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

    def rendering_engines():
        return [
            "Octane Render",
            "Ray Tracing",
            "Unreal Engine",
            "V-Ray",
            "{{rendering_engine}}",
        ]

    def lightning_angles():
        return [
            "Back Light",
            "Front Light",
            "Light From Left",
            "Light From Right",
            "Top Light",
            "{{lightning_angle}}",
        ]

    def lightning_styles():
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

    def camera_positions():
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

    def cameras():
        return [
            "Canon",
            "Leica M",
            "Leica" "Nikon",
            "Sony alpha",
            "{{camera}}",
        ]

    def camera_styles():
        return [
            "Early Wet Plate",
            "Fisheye",
            "Golden hour",
            "Infrared",
            "Kodachrome",
            "Long Exposure",
            "Macro",
            "Polaroid",
            "{{camera_style}}",
        ]

    def compositions():
        return [
            "Asymetric",
            "Centered",
            "Golden Ratio",
            "Symmetrical",
            "Triangular Composition",
            "{{composition}}",
        ]

    def isos():
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

    def resolutions():
        return [
            "{{resolution}}",
            "8k",
            "HD",
            "Full HD",
        ]

    def generate(self, **kwargs):
        description = kwargs["description"] if "description" in kwargs else None
        time = kwargs["time"] if "time" in kwargs else None
        type = kwargs["type"] if "type" in kwargs else None
        background_color = (
            kwargs["background_color"] if "background_color" in kwargs else None
        )
        art_style = kwargs["art_style"] if "art_style" in kwargs else None
        artist = kwargs["artist"] if "artist" in kwargs else None
        realism = kwargs["realism"] if "realism" in kwargs else None
        rendering_engine = (
            kwargs["rendering_engine"] if "rendering_engine" in kwargs else None
        )
        lightning_angle = (
            kwargs["lightning_angle"] if "lightning_angle" in kwargs else None
        )
        lightning_style = (
            kwargs["lightning_style"] if "lightning_style" in kwargs else None
        )
        camera_position = (
            kwargs["camera_position"] if "camera_position" in kwargs else None
        )
        camera = kwargs["camera"] if "camera" in kwargs else None
        camera_style = kwargs["camera_style"] if "camera_style" in kwargs else None
        composition = kwargs["composition"] if "composition" in kwargs else None
        iso = kwargs["iso"] if "iso" in kwargs else None
        resolution = kwargs["resolution"] if "resolution" in kwargs else None
        compel_style = kwargs["compel_style"] if "compel_style" in kwargs else None

        separator = ", "

        context = []
        prompt = []
        style = []
        image = []

        if time != None:
            context.append(time)
        if type != None:
            context.append(type)

        prompt = [x.strip() for x in description] if description != None else []

        if background_color != None:
            style.append("with background " + background_color)
        if art_style != None and len(art_style) > 0:
            style.append(separator.join(art_style))
        if artist != None and len(artist) > 0:
            style.append("by " + separator.join(artist))

        if realism != None and len(realism) > 0:
            image.append(separator.join(realism))
        if rendering_engine != None and len(rendering_engine) > 0:
            image.append(separator.join(rendering_engine))
        if lightning_angle != None and len(lightning_angle) > 0:
            image.append(separator.join(lightning_angle))
        if lightning_style != None and len(lightning_style) > 0:
            image.append(separator.join(lightning_style))
        if camera_position != None and len(camera_position) > 0:
            image.append(separator.join(camera_position))
        if camera != None and len(camera) > 0:
            image.append(separator.join(camera))
        if camera_style != None and len(camera_style) > 0:
            image.append(separator.join(camera_style))
        if composition != None and len(composition) > 0:
            image.append(separator.join(composition))
        if iso != None:
            image.append(iso)
        if resolution != None and len(resolution) > 0:
            image.append(separator.join(resolution))

        if compel_style == "subtle":
            segments = []
            lead = []
            if len(context) > 0:
                lead += [" ".join(context)]
            if len(prompt) > 0:
                lead += prompt
            if len(style) > 0:
                lead += style
            if len(lead) > 0:
                segments.append(separator.join(["'" + x + "'" for x in lead]))
            if len(image) > 0:
                segments.append("'" + separator.join(image) + "'")
            return "({0}).and()".format(separator.join(segments))
        elif compel_style == "full":
            segments = []
            if len(context) > 0:
                segments.append("'" + " ".join(context) + "'")
            if len(prompt) > 0:
                segments.append(separator.join(["'" + x + "'" for x in prompt]))
            if len(style) > 0:
                segments.append("'" + separator.join(style) + "'")
            if len(image) > 0:
                segments.append("'" + separator.join(image) + "'")
            return "({0}).and()".format(separator.join(segments))
        else:
            return separator.join(context + prompt + style + image)
