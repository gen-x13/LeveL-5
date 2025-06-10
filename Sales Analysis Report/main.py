""" #genxcode - Sales analysis """

# Module's Importation
import io
import pandas as pd
from io import BytesIO
import streamlit as st
import plotly.io as pio
import plotly.express as px
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu


# Session State

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False  

# Define

upload_file = None # Initialization


# Menu

with st.sidebar:
    selected=option_menu(
        menu_title="Menu",
        options = ["Home", "Français", "English"],
        icons = ["house-door", "clipboard2-data", "clipboard2-data"],
        menu_icon="menu-button-wide",
        default_index=0
        )


# Home Page

if selected == "Home":
    
    st.title("AutoSales Report Generator")
    
    # English Version
    
    st.subheader("Sale analysis website")
    st.text("")
    
    st.markdown("This site has been designed to provide you with a ***complete*** and ***automated*** analysis of your weekly sales.")
    st.markdown("Simply upload your CSV file, and within moments you'll receive a clear, detailed report in PDF format, ready to share or archive.")
    st.markdown("An interface available in **French** and **English** to suit your audience.")
    st.markdown("This version is a **free** prototype, a stepping stone towards a more advanced version incorporating machine learning.")
    st.markdown("Please find below :violet[**my GitHub portfolio**], :red[**my Youtube channel**] and :blue[**my Ko-Fi profile**] , if you'd like to support this project or explore my other creations.")
    
    st.text("---")
    
    # French Version
    
    st.subheader("Site web d'analyse des ventes")
    st.text("")
    
    st.markdown("Ce site a été conçu pour vous fournir une analyse ***complète*** et ***automatisée*** de vos ventes hebdomadaires.")
    st.markdown("Il vous suffit de télécharger votre fichier CSV et, en quelques instants, vous recevrez un rapport clair et détaillé au format PDF, prêt à être partagé ou archivé.")
    st.markdown("Une interface disponible en **français** et **anglais** pour s'adapter à votre public.")
    st.markdown("Cette version est un prototype **gratuit**, un tremplin vers une version plus avancée intégrant l'apprentissage automatique.")
    st.markdown("Vous trouverez ci-dessous :violet[**mon portfolio GitHub**], :red[**ma chaîne Youtube**] et :blue[**mon profil Ko-Fi**] , si vous souhaitez soutenir ce projet ou découvrir mes autres créations.")
    
    st.text("---")
    
    st.markdown("You can leave a feedback and follow me on my social medias.")
    
    
    # Stars Feedback
    
    sentiment_mapping = ["one", "two", "three", "four", "five"]
    selected = st.feedback("stars")
    
    if selected is not None:
        st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
    
    
    st.text("")    
    st.text("")
    
    
    # Logos
    
    components.html('''
<div style="display: flex; justify-content: center; gap: 40px; align-items: center;">
  <a href="https://github.com/gen-x13" target="_blank">
    <svg xmlns="http://www.w3.org/2000/svg" width="80" height="80" fill="currentColor" class="bi bi-github" viewBox="0 0 16 16">
      <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27s1.36.09 2 .27c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8"/>
    </svg>
  </a>

  <a href="https://www.youtube.com/@genxcodeofficial" target="_blank">
    <svg xmlns="http://www.w3.org/2000/svg" width="80" height="80" fill="#FF0000" viewBox="0 0 16 16">
      <path d="M8.051 1.999h-.002C3.638 1.999 1.684 2.158 1.04 2.316c-.632.156-1.132.654-1.29 1.287C-.211 4.633-.364 6.588-.364 8c0 1.41.153 3.367.414 4.397.158.633.658 1.131 1.29 1.287.644.158 2.598.316 7.011.316s6.367-.158 7.011-.316c.632-.156 1.132-.654 1.29-1.287.261-1.03.414-2.987.414-4.397 0-1.412-.153-3.367-.414-4.397-.158-.633-.658-1.131-1.29-1.287-.644-.158-2.598-.317-7.011-.317zM6.5 5.5l4 2.5-4 2.5v-5z"/>
    </svg>
  </a>

  <a href="https://ko-fi.com/genxcodeofficial" target="_blank">
    <svg xmlns="http://www.w3.org/2000/svg" width="80" height="80" fill="#29ABE0" viewBox="0 0 512 512">
      <path d="M410.2 162.6c0-16.1-13.1-29.2-29.2-29.2H97.9c-21.3 0-38.6 17.3-38.6 38.6v168.2c0 55.2 44.8 100 100 100H314c55.2 0 100-44.8 100-100v-76.9h21.2c33.7 0 61.1-27.4 61.1-61.1s-27.4-61-61.1-61H410.2zm0 61.1v-61.1h21.2c16.8 0 30.4 13.6 30.4 30.4s-13.6 30.4-30.4 30.4h-21.2zM169 311.6c-23.2-19.1-38.5-37.8-38.5-61.5 0-23.3 18.9-42.2 42.2-42.2 14.5 0 27.6 7.2 35.6 18.2 8-11 21.1-18.2 35.6-18.2 23.3 0 42.2 18.9 42.2 42.2 0 23.7-15.3 42.3-38.5 61.5-8.6 7.1-18.3 14-28.2 20.6-9.9-6.5-19.6-13.5-28.2-20.6z"/>
    </svg>
  </a>
</div>
''', height=200)



# Visualization French Page

elif selected == "Français":
    

    st.title("Analyse de vos ventes")
    st.text("")

    st.header('Importez votre fichier CSV, ci-dessous :')
    st.markdown('Veillez à supprimer les valeurs manquantes et les doublons avant de continuer.')
    st.markdown('La version PRO, qui sortira prochainement, le fera pour vous en 1 clic.')
    
    st.text("")

    upload_file = st.file_uploader("Glisser et déposer un fichier ici :",
                                   accept_multiple_files=False, 
                                   on_change= lambda: analyze(upload_file),  
                                   label_visibility="visible")
    
    
# Visualization English Page

elif selected == "English":
    
    
    st.title("Analysis of your sales")
    st.text("")
       
    st.header('Import your CSV file, below :')
    st.markdown('Be sure to delete missing values and duplicates before continuing.')
    st.markdown('The PRO version, coming soon, will do it for you in 1 click.')
    
    st.text("")

    upload_file = st.file_uploader("Drag and drop one file here :",
                                   accept_multiple_files=False, 
                                   on_change= lambda: analyze(upload_file), 
                                   label_visibility="visible")



# Analysis Function

def analyze(upload_file):
    
    
    if upload_file is not None:
        
        df = pd.read_csv(upload_file)
        
        st.session_state.disabled = "visible"
        
        if selected == "Français":
            
            st.info('Votre fichier a été importé avec succès.', icon="ℹ️")
            
        else:
            
            st.info('Your file had been imported successfully', icon="ℹ️")
            
        
        st.dataframe(df)
        
        
                             ### FRENCH PART ###    
        
        
        if selected == "Français":
            
            col = st.selectbox(
                                "Choisissez la colonne :", 
                                df.columns,
                                index=None,
                                placeholder= "Sélectionnez une colonne...",
                                label_visibility=st.session_state.visibility)
            
            group_col = st.selectbox(
                                "Grouper par quelle colonne ? (optionnel)",
                                options=[None] + list(df.columns),
                                index=0,
                                format_func=lambda x: "Aucun regroupement" if x is None else x,
                                placeholder="Sélectionnez une colonne...",
                                label_visibility=st.session_state.visibility
                            )
            
            if col and group_col:
                
                choix_type = st.selectbox("Choisissez un type de graphique :",
                                          ["Ligne", "Barre", "Points"],
                                          index=None,
                                          placeholder= "Sélectionnez un type...",
                                          label_visibility=st.session_state.visibility)
                
                # Grouping data columns
                grouped = df.groupby(group_col)[col].mean().reset_index()  
                
                # Stocking variables
                title_grcol_text = f"Visualisation de la moyenne entre {col} et {group_col} - Graphique en {choix_type}"
                valeur = round(df[col].mean(), 2)
                gr_text = f"Moyenne de {col} : {valeur}"
                
                
                # Type choice
                if choix_type == "Ligne":
                    
                    st.write(title_grcol_text)
               
                    gr_ligne = px.line(grouped, x=group_col, y=col)
                    
                    st.metric(f"Moyenne de {col}", valeur)

                    
                elif choix_type == "Barre":
                    
                    st.write(title_grcol_text)
                    
                    gr_barre = px.bar(grouped, x=group_col, y=col)
                    
                    st.metric(f"Moyenne de {col}", valeur)

                    
                elif choix_type == "Points":
                    
                    st.write(title_grcol_text)
                    
                    gr_point = px.scatter(grouped, x=group_col, y=col)
                    
                    st.metric(f"Moyenne de {col}", valeur)

                
                
            elif col:
                
                analyses_fr = {
                    
                        "Moyenne": df[col].mean,
                        "Médiane": df[col].median,
                        "Mode": lambda: df[col].mode().tolist(),
                        "Écart-type": df[col].std,
                        "Variance": df[col].var,
                        "Minimum": df[col].min,
                        "Maximum": df[col].max,
                        "Somme": df[col].sum,
                        "Nombre de valeurs": df[col].count,
                        "Valeurs uniques": df[col].nunique
                        
                        }
                
                choix_analyse = st.selectbox("Choisissez une analyse :", 
                                             list(analyses_fr.keys()),
                                             index=None,
                                             placeholder= "Sélectionnez une analyse...",
                                             label_visibility=st.session_state.visibility)
                
                if choix_analyse is not None:
                    
                    choix_type = st.selectbox("Choisissez un type de graphique :",
                                              ["Ligne", "Barre", "Points"],
                                              index=None,
                                              placeholder= "Sélectionnez un type...",
                                              label_visibility=st.session_state.visibility)
                    
                    # Stocking variables
                    title_col_text = f"Visualisation de la colonne {col} - Analyse : {choix_analyse} - Graphique en {choix_type}"
                    valeur = analyses_fr[choix_analyse]()
                    col_text = f"{choix_analyse} de {col} : {valeur}"
                    
                    # Type Choice
                    if choix_type == "Ligne":
                        
                        st.write(title_col_text)
                        
                        # Chart
                        ligne = px.line(df, y=col)
                        
                        #Metrique
                        m_ligne = st.metric(f"{choix_analyse} de {col}", valeur)

                    
                    elif choix_type == "Barre":
                        
                        st.write(title_col_text)
                        
                        barre = px.bar(df, y=col)
                        
                        m_barre = st.metric(f"{choix_analyse} de {col}", valeur)
                        
                        
                    elif choix_type == "Points":
                        
                        st.write(title_col_text)
                        
                        point = px.scatter(df, y=col)
                        
                        m_point = st.metric(f"{choix_analyse} de {col}", valeur)
                        
            st.text("")
            
            
            class Graphique:
                
                def __init__(self, titre, type_graphe, metrique=None, nom="Graphique"):
                    
                    self.titre = titre
                    self.type_graphe = type_graphe
                    self.metrique = metrique
                    self.nom = nom
            
            # State of graph_list
            if "graph_list" not in st.session_state:
                
                st.session_state.graph_list = []
            
            # Add graph function
            def ajouter_graphique(dico, nom_graph):
                
                for key, (titre, type_g, metrique) in dico.items():
                    
                    if type_g:
                        
                        new_graph = Graphique(titre, type_g, metrique, nom=nom_graph)
                        st.session_state.graph_list.append(new_graph)
            
                        st.success(f"{nom_graph} ajouté !", icon="✅")
                        
                        return 
            
                
                st.warning("Aucun graphique ajouté.")
            
            
            
            if st.button("Ajouter un graphique"):
            
                n = len(st.session_state.graph_list) + 1
                nom_graph = f"Graphique {n}"
                
                if col and group_col:
                    
                    gr_dico = {}
            
                    if choix_type == "Ligne":
                        gr_dico["gr_ligne"] = (title_grcol_text, gr_ligne, gr_text)
            
                    elif choix_type == "Barre":
                        gr_dico["gr_barre"] = (title_grcol_text, gr_barre, gr_text)
            
                    elif choix_type == "Points":
                        gr_dico["gr_point"] = (title_grcol_text, gr_point, gr_text)
            
                    ajouter_graphique(gr_dico, nom_graph)
            
                
                elif col and not group_col:
                    
                    dico = {}
            
                    if choix_type == "Ligne":
                        dico["ligne"] = (title_col_text, ligne, col_text)
            
                    elif choix_type == "Barre":
                        dico["barre"] = (title_col_text, barre, col_text)
            
                    elif choix_type == "Points":
                        dico["point"] = (title_col_text, point, col_text)
            
                    ajouter_graphique(dico, nom_graph)
            
                else:
                    
                    st.warning("Aucun graphique ajouté.")
    
                            
                
            #Import graph's name
            st.markdown("### Graphiques enregistrés :")
            
            for g in st.session_state.graph_list:
                st.write(f"**{g.nom}**")
            
            # Selection graph order
            options = [g.nom for g in st.session_state.graph_list]
            selection = st.pills("Veuillez sélectionner l'ordre d'affichage des graphiques :", options, selection_mode="multi")
            st.markdown(f"L'ordre d'affichage : {selection}.")
            
            # Input text for PDF
            pdf_titre = st.text_input("Titre du rapport")
            pdf_auteur = st.text_input("Auteur")
            pdf_compagnie = st.text_input("Entreprise")
            pdf_datefr = st.text_input("Date")

            # Generating function
            def genere_pdf():
                
                buffer = io.BytesIO() #create a file in memory
                
                myCanvas = canvas.Canvas(buffer, pagesize=A4)

                w, h = A4
                

                myCanvas.setFont("Helvetica", 20)
                myCanvas.drawString(150, h - 40, pdf_titre)
                
                h -= 40
                
                # Displaying each graph
                for g in st.session_state.graph_list:
                    
                    if g.nom in selection:
                        
                        f = io.BytesIO()
                        pio.write_image(g.type_graphe, f, format="png")
                        f.seek(0)
                        
                        image = ImageReader(f)
                        
                        # Si pas assez de place : nouvelle page
                        if h - 300 < 100:
                            myCanvas.showPage()
                            h = A4[1] - 100
                        
                        h -= 30
                        
                        myCanvas.setFont("Helvetica-Bold", 12)
                        myCanvas.drawString(50, h, getattr(g, 'titre', ""))
                        
                        h -= 200
                        myCanvas.drawImage(image, 50, h - 30, width=400, height=200)
                        
                        h -= 30
                        myCanvas.setFont("Helvetica", 10)
                        
                        text_value2 = getattr(g, 'metrique', "")
                        
                        # Transforming bytes into string
                        if isinstance(text_value2, bytes):
                            text_value2 = text_value2.decode("utf-8")  # or whatever encoding you're using
                        elif not isinstance(text_value2, str):
                            text_value2 = str(text_value2)
                            
                        myCanvas.drawString(50, h - 10, text_value2)
                        
                        h -= 20
                    
                    # Footer
                    myCanvas.setFont("Helvetica", 10)
                    page_num = myCanvas.getPageNumber()
                    text = "Page %s" % page_num
                    myCanvas.drawString(w/2, 10, text)
            
                myCanvas.setFont("Helvetica", 10)
                myCanvas.drawString(30, 60, pdf_auteur)
                myCanvas.drawString(30, 50, pdf_compagnie)
                myCanvas.drawString(30, 40, pdf_datefr)
            
                myCanvas.save()
                
                # Recovers PDF content
                buffer.seek(0)
                return buffer
            
            # Use genere_pdf function
            pdf_file = genere_pdf()
            
            #Download it to pdf
            st.download_button(
                
                        label="Télécharger l’analyse en PDF",
                        data=pdf_file,
                        file_name="analyse.pdf",
                        mime="application/pdf"
                    )
                

                
                
                             ### ENGLISH PART ###       
                
        
        elif selected == "English":
           
            col = st.selectbox(
                                "Choose column:", 
                                df.columns,
                                index=None,
                                placeholder= "Select a column...",
                                label_visibility=st.session_state.visibility)
            
            group_col = st.selectbox(
                                "Group by which column (optional)",
                                options=[None] + list(df.columns),
                                index=0,
                                format_func=lambda x: "No regrouping" if x is None else x,
                                placeholder="Select a column...",
                                label_visibility=st.session_state.visibility
                            )
            
            if col and group_col:
                
                choice_type = st.selectbox("Choose a chart type:",
                                          ["Line", "Bar", "Scatter"],
                                          index=None,
                                          placeholder= "Select a type...",
                                          label_visibility=st.session_state.visibility)
                
                grouped = df.groupby(group_col)[col].mean().reset_index()
                
                title_grcol = f"Visualization of the average between {col} and {group_col} - Graph in {choice_type}."
                value = round(df[col].mean(), 2)
                gr_text = f"Mean of {col} : {value}"
                
                if choice_type == "Line":
               
                    gr_line = px.line(grouped, x=group_col, y=col)
                    gr_mline = st.metric(f"Mean of {col}", value)

                    
                elif choice_type == "Bar":
                    
                    gr_bar = px.bar(grouped, x=group_col, y=col)
                    gr_mbar = st.metric(f"Mean of {col}", value)

                    
                elif choice_type == "Scatter":
                    
                    gr_scatter = px.scatter(grouped, x=group_col, y=col)
                    gr_mscatter = st.metric(f"Mean of {col}", value)

                
                
            elif col:
                
                analysis_en = {
                    
                        "Mean": df[col].mean,
                        "Median": df[col].median,
                        "Mode": lambda: df[col].mode().tolist(),
                        "Standard deviation": df[col].std,
                        "Variance": df[col].var,
                        "Minimum": df[col].min,
                        "Maximum": df[col].max,
                        "Sum": df[col].sum,
                        "Number of values": df[col].count,
                        "Unique values": df[col].nunique
                        
                        }
                
                choice_analysis = st.selectbox("Choose an analysis :", 
                                             list(analysis_en.keys()),
                                             index=None,
                                             placeholder= "Select an analysis :",
                                             label_visibility=st.session_state.visibility)
                
                if choice_analysis is not None:
                    
                    choice_type = st.selectbox("Choose a chart type :",
                                              ["Line", "Bar", "Scatter"],
                                              index=None,
                                              placeholder= "Select a type...",
                                              label_visibility=st.session_state.visibility)
                    
                    # Stocking Variables
                    title_col = f"Visualization of column {col} - Analysis: {choice_analysis} - Graph in {choice_type}"
                    value = analysis_en[choice_analysis]()
                    col_text = f"{choice_analysis} of {col} : {value}"
                    
                    if choice_type == "Line":
                                                
                        # Chart
                        
                        line = px.line(df, y=col)
                        m_line = st.metric(f"{choice_analysis} of {col}", value)

                    
                    elif choice_type == "Bar":
                     
                        # Chart
                        bar = px.bar(df, y=col)
                        m_bar= st.metric(f"{choice_analysis} of {col}", value)
                        
                        
                    elif choice_type == "Scatter":
                     
                        # Chart
                        scatter = px.scatter(df, y=col)
                        m_scatter = st.metric(f"{choice_analysis} of {col}", value)
                        
            st.text("")
            
            class Graphic:
                
                def __init__(self, title, graph_type, metric, name="Graphic"):
                    
                    self.title = title
                    self.graphe_type = graph_type
                    self.metric = metric
                    self.name = name
                    
            if "graph_list" not in st.session_state:

                st.session_state.graph_list = []
            
            def add_graphic(dico, name_graph):
                
                for key, (title, g_type, metric) in dico.items():
            
                    
                    if g_type:
                        
                        new_graph = Graphic(title, g_type, metric, name=name_graph)
                        st.session_state.graph_list.append(new_graph)
            
                        st.success(f"{name_graph} added !", icon="✅")
                        
                        return 
            
                
                st.warning("No charts added.")
            
            
            if st.button("Add a graph"):
            
                n = len(st.session_state.graph_list) + 1
                name_graph = f"Graphic {n}" 
            
                
                if col and group_col:
                    
                    gr_dico = {}
            
                    if choice_type == "Line":
                        gr_dico["gr_line"] = (title_grcol, gr_line, gr_text)
            
                    elif choice_type == "Bar":
                        gr_dico["gr_bar"] = (title_grcol, gr_bar, gr_text)
            
                    elif choice_type == "Scatter":
                        gr_dico["gr_scatter"] = (title_grcol, gr_scatter, gr_text)
            
                    add_graphic(gr_dico, name_graph)
            
                
                elif col and not group_col:
                    
                    dico = {}
            
                    if choice_type == "Line":
                        dico["line"] = (title_col, line, col_text)
            
                    elif choice_type == "Bar":
                        dico["bar"] = (title_col, bar, col_text)
            
                    elif choice_type == "Scatter":
                        dico["scatter"] = (title_col, scatter, col_text)
            
                    add_graphic(dico, name_graph)
            
                else:
                    st.warning("No charts added.")

                            
            # Import graph's name    
            st.markdown("### Recorded graphics :")
            
            for g in st.session_state.graph_list:
                st.write(f"**{g.name}**")
                
            # Selection graph order
            options = [g.name for g in st.session_state.graph_list]
            selection = st.pills("Please select the order in which the graphs are displayed:", options, selection_mode="multi")
            st.markdown(f"Display order: {selection}.")
                
            # Input's form    
            pdf_title = st.text_input("Report's Title")
            pdf_author = st.text_input("Author")
            pdf_company = st.text_input("Company")
            pdf_dateen = st.text_input("Date")


            # Generating function
            def genere_pdf():
                
                buffer = io.BytesIO() #create a file in memory
                
                myCanvas = canvas.Canvas(buffer, pagesize=A4)

                w, h = A4
                

                myCanvas.setFont("Helvetica", 20)
                myCanvas.drawString(150, h - 40, pdf_title)
                
                h -= 40
                
                # Displaying each graph
                for g in st.session_state.graph_list:
                    
                    if g.name in selection:
                        
                        f = io.BytesIO()
                        pio.write_image(g.graph_type, f, format="png")
                        f.seek(0)
                        
                        image = ImageReader(f)
                        
                        # Si pas assez de place : nouvelle page
                        if h - 300 < 100:
                            myCanvas.showPage()
                            h = A4[1] - 100
                        
                        h -= 30
                        
                        myCanvas.setFont("Helvetica-Bold", 12)
                        myCanvas.drawString(50, h, getattr(g, 'title', ""))
                        
                        h -= 200
                        myCanvas.drawImage(image, 50, h - 30, width=400, height=200)
                        
                        h -= 30
                        myCanvas.setFont("Helvetica", 10)
                        
                        text_value2 = getattr(g, 'metric', "")
                        
                        # Transforming bytes into string
                        if isinstance(text_value2, bytes):
                            text_value2 = text_value2.decode("utf-8")  # or whatever encoding you're using
                        elif not isinstance(text_value2, str):
                            text_value2 = str(text_value2)
                            
                        myCanvas.drawString(50, h - 10, text_value2)
                        
                        h -= 20
                    
                    # Footer
                    myCanvas.setFont("Helvetica", 10)
                    page_num = myCanvas.getPageNumber()
                    text = "Page %s" % page_num
                    myCanvas.drawString(w/2, 10, text)
            
                myCanvas.setFont("Helvetica", 10)
                myCanvas.drawString(30, 60, pdf_author)
                myCanvas.drawString(30, 50, pdf_company)
                myCanvas.drawString(30, 40, pdf_dateen)
            
                myCanvas.save()
                
                # Recovers PDF content
                buffer.seek(0)
                return buffer
            
            # Use genere_pdf function
            pdf_file = genere_pdf()
            
            #Download it to pdf
            st.download_button(
                
                        label="Download your analysis in PDF",
                        data=pdf_file,
                        file_name="analysis.pdf",
                        mime="application/pdf"
                    )
            
        else:
            st.warning("There's an error. Retry.")
            
                    
if upload_file is not None:
    
    analyze(upload_file)

    
    

