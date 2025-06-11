import customtkinter as ctk
class AggiungiSchedaClientePage(ctk.CTkFrame):
    def __init__(self, master, cliente_id, back_callback=None):
        super().__init__(master)

        self.cliente_id = cliente_id
        self.back_callback = back_callback

        #Frame principale scorrevole
        self.content_frame = ctk.CTkScrollableFrame(
            master=self,
            corner_radius=10,
            fg_color="#2e2e3e"
        )
        self.content_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Configuro la colonna 0 di content_frame per espandersi
        self.content_frame.grid_columnconfigure(0, weight=1)

        # Header (titolo + Indietro) su un'unica riga
        header_frame = ctk.CTkFrame(
            master=self.content_frame,
            corner_radius=0,
            fg_color="transparent"
        )
        header_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 20))
        header_frame.grid_columnconfigure(0, weight=1)
        header_frame.grid_columnconfigure(1, weight=0)

        titolo = ctk.CTkLabel(
            master=header_frame,
            text="Aggiungi Scheda Cliente",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="#ffffff"
        )
        titolo.grid(row=0, column=0, sticky="w")

        back_button = ctk.CTkButton(
            master=header_frame,
            text="« Indietro",
            height=36,
            corner_radius=8,
            fg_color="#3a3a4d",
            hover_color="#4a4a5d",
            text_color="#ffffff",
            font=ctk.CTkFont(size=14),
            command=self.back_callback
        )
        back_button.grid(row=0, column=1, sticky="e")

        # Form per l'inserimento dei dati della scheda di un cliente 

        form_frame = ctk.CTkFrame(
            master=self.content_frame,
            corner_radius=10,
            fg_color="#3a3a4d"
        )
        form_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=(0, 20))
        form_frame.grid_columnconfigure(0, weight=1)
        form_frame.grid_columnconfigure(1, weight=1)

        # Etichette e campi di input per i dati della scheda

        # Peso

        ctk.CTkLabel(
            master=form_frame,
            text="Peso:",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#ffffff"
        ).grid(row=0, column=0, sticky="w", padx=10, pady=(10, 5))

        self.peso_entry = ctk.CTkEntry(
            master=form_frame,
            placeholder_text="Kg",
            font=ctk.CTkFont(size=14),
            width=200,
            fg_color="#3a3a4d",
            text_color="#ffffff"
        )
        self.peso_entry.grid(row=1, column=0, sticky="ew", padx=10, pady=(10, 5))

        # Altezza

        ctk.CTkLabel(
            master=form_frame,
            text="altezza:",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#ffffff"
        ).grid(row=0, column=1, sticky="w", padx=10, pady=(10, 5))

        self.aletzza_entry = ctk.CTkEntry(
            master=form_frame,
            placeholder_text="cm",
            font=ctk.CTkFont(size=14),
            width=200,
            fg_color="#3a3a4d",
            text_color="#ffffff"
        )
        self.aletzza_entry.grid(row=1, column=1, sticky="ew", padx=10, pady=(10, 5))

        # Massa Muscolare

        ctk.CTkLabel(
            master=form_frame,
            text="Massa Muscolare:",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#ffffff"
        ).grid(row=2, column=0, sticky="w", padx=10, pady=(10, 5))

        self.massa_muscolare_entry = ctk.CTkEntry(
            master=form_frame,
            placeholder_text="Kg",
            font=ctk.CTkFont(size=14),
            width=200,
            fg_color="#3a3a4d",
            text_color="#ffffff"
        )
        self.massa_muscolare_entry.grid(row=3, column=0, sticky="ew", padx=10, pady=(10, 5))

        # Massa grassa

        ctk.CTkLabel(
            master=form_frame,
            text="Massa Grassa:",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#ffffff"
        ).grid(row=2, column=1, sticky="w", padx=10, pady=(10, 5))

        self.peso_entry = ctk.CTkEntry(
            master=form_frame,
            placeholder_text="Kg",
            font=ctk.CTkFont(size=14),
            width=200,
            fg_color="#3a3a4d",
            text_color="#ffffff"
        )
        self.peso_entry.grid(row=3, column=1, sticky="ew", padx=10, pady=(10, 5))

        # bmi

        ctk.CTkLabel(
            master=form_frame,
            text="bmi:",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#ffffff"
        ).grid(row=4, column=0, sticky="w", padx=10, pady=(10, 5))

        self.bmi_entry = ctk.CTkEntry(
            master=form_frame,
            placeholder_text="peso / (altezza * 2)",
            font=ctk.CTkFont(size=14),
            width=200,
            fg_color="#3a3a4d",
            text_color="#ffffff"
        )
        self.bmi_entry.grid(row=5, column=0, sticky="ew", padx=10, pady=(10, 5))

        # Note

        ctk.CTkLabel(
            master=form_frame,
            text="Note",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#ffffff"
        ).grid(row=6, column=0, columnspan = 2,sticky="w", padx=10, pady=(10, 5))

        self.nome_entry = ctk.CTkEntry(
            master=form_frame,
            placeholder_text="peso / (altezza * 2)",
            font=ctk.CTkFont(size=14),
            width=200,
            fg_color="#3a3a4d",
            text_color="#ffffff"
        )
        self.note_entry.grid(row=7, column=0, columnspan = 2, sticky="ew", padx=10, pady=(10, 5))


















