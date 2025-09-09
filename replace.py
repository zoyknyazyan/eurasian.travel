import os

# Set your root directory
root_dir = 'travel-visa/'

# First, let's extract the exact old nav from one of your files
sample_file = 'travel-visa/andorra-e-visa-in-word-and-pdf-template.html'  # Use one of your actual files
with open(sample_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the nav section (this will help us get the exact formatting)
start_marker = '<nav id="site-navigation" class="main-navigation"'
end_marker = '</nav>'
start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx) + len(end_marker)

if start_idx != -1 and end_idx != -1:
    exact_old_nav = content[start_idx:end_idx]
    print("Found exact old nav pattern")
else:
    print("Could not find nav in sample file")
    exit()

# Your new nav (as you provided)
new_nav = '''<nav id="site-navigation" class="main-navigation" itemscope
                        itemtype="https://schema.org/SiteNavigationElement">
                        <div class="menu-barra-navigazione-container">
                            <ul id="primary-menu" class="menu">
                                <li id="menu-item-26"
                                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-home menu-item-26">
                                    <a href="../index.html">Home</a>
                                </li>
                                <li id="menu-item-31"
                                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-31"><a
                                        href="../destination.html">Destinazioni</a></li>
                                <li id="menu-item-30"
                                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-30">
                                    <a href="../esperienze.html">Esperienze</a>
                                    <ul class="sub-menu">
                                        <li id="menu-item-46"
                                            class="menu-item menu-item-type-custom menu-item-object-custom current-menu-ancestor current-menu-parent menu-item-has-children menu-item-46">
                                            <a>Attività</a>
                                            <ul class="sub-menu">
                                                <li id="menu-item-45"
                                                    class="menu-item menu-item-type-custom menu-item-object-custom current-menu-item menu-item-45">
                                                    <a href="../activities/arte-cultura.html"
                                                        aria-current="page">Arte&#038;Cultura</a>
                                                </li>
                                                <li id="menu-item-47"
                                                    class="menu-item menu-item-type-custom menu-item-object-custom menu-item-47">
                                                    <a href="../activities/avventura.html">Avventura</a>
                                                </li>
                                                <li id="menu-item-48"
                                                    class="menu-item menu-item-type-custom menu-item-object-custom menu-item-48">
                                                    <a href="../activities/evento.html">Evento</a>
                                                </li>
                                                <li id="menu-item-49"
                                                    class="menu-item menu-item-type-custom menu-item-object-custom menu-item-49">
                                                    <a href="../activities/montagna.html">Montagna</a>
                                                </li>
                                                <li id="menu-item-50"
                                                    class="menu-item menu-item-type-custom menu-item-object-custom menu-item-50">
                                                    <a href="../activities/mare.html">Mare</a>
                                                </li>
                                                <li id="menu-item-51"
                                                    class="menu-item menu-item-type-custom menu-item-object-custom menu-item-51">
                                                    <a href="../activities/crociere.html">Crociere</a>
                                                </li>
                                                <li id="menu-item-52"
                                                    class="menu-item menu-item-type-custom menu-item-object-custom menu-item-52">
                                                    <a href="../activities/relax.html">Relax</a>
                                                </li>
                                                <li id="menu-item-53"
                                                    class="menu-item menu-item-type-custom menu-item-object-custom menu-item-53">
                                                    <a href="../activities/romantico.html">Romantico</a>
                                                </li>
                                                <li id="menu-item-54"
                                                    class="menu-item menu-item-type-custom menu-item-object-custom menu-item-54">
                                                    <a href="../activities/esclusivo.html">Esclusivo</a>
                                                </li>
                                            </ul>
                                        </li>
                                        <li id="menu-item-55"
                                            class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-55">
                                            <a>Tipo</a>
                                            <ul class="sub-menu">
                                                <li id="menu-item-56"
                                                    class="menu-item menu-item-type-custom menu-item-object-custom menu-item-56">
                                                    <a href="../trip-types/individuale.html">Individuale</a>
                                                </li>
                                                <li id="menu-item-57"
                                                    class="menu-item menu-item-type-custom menu-item-object-custom menu-item-57">
                                                    <a href="../trip-types/gruppo.html">Gruppo</a>
                                                </li>
                                                <li id="menu-item-58"
                                                    class="menu-item menu-item-type-custom menu-item-object-custom menu-item-58">
                                                    <a href="../trip-types/viaggi-di-nozze.html">Viaggi di Nozze</a>
                                                </li>
                                                <li id="menu-item-59"
                                                    class="menu-item menu-item-type-custom menu-item-object-custom menu-item-59">
                                                    <a href="../trip-types/viaggi-di-coppia.html">Viaggi di Coppia</a>
                                                </li>
                                                <li id="menu-item-60"
                                                    class="menu-item menu-item-type-custom menu-item-object-custom menu-item-60">
                                                    <a href="../404.html">Business</a>
                                                </li>
                                                <li id="menu-item-61"
                                                    class="menu-item menu-item-type-custom menu-item-object-custom menu-item-61">
                                                    <a href="../trip-types/garantiti-per-due.html">Partenza
                                                        garantita</a>
                                                </li>
                                                <li id="menu-item-266"
                                                    class="menu-item menu-item-type-custom menu-item-object-custom menu-item-266">
                                                    <a href="../trip-types/con-accompagnatore.html">Con
                                                        accompagnatore</a>
                                                </li>
                                                <li id="menu-item-267"
                                                    class="menu-item menu-item-type-custom menu-item-object-custom menu-item-267">
                                                    <a href="../trip-types/scuola.html">Scuola</a>
                                                </li>
                                            </ul>
                                        </li>
                                        <li id="menu-item-62"
                                            class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-62">
                                            <a>Adatto</a>
                                            <ul class="sub-menu">
                                                <li id="menu-item-63"
                                                    class="menu-item menu-item-type-custom menu-item-object-custom menu-item-63">
                                                    <a href="../activities/bambini.html">Bambini</a>
                                                </li>
                                                <li id="menu-item-64"
                                                    class="menu-item menu-item-type-custom menu-item-object-custom menu-item-64">
                                                    <a href="../activities/mobilita-ridotta.html">Mobilità ridotta</a>
                                                </li>
                                                <li id="menu-item-65"
                                                    class="menu-item menu-item-type-custom menu-item-object-custom menu-item-65">
                                                    <a href="../404.html">Adulti</a>
                                                </li>
                                                <li id="menu-item-66"
                                                    class="menu-item menu-item-type-custom menu-item-object-custom menu-item-66">
                                                    <a href="../activities/sportivi.html">Sportivi</a>
                                                </li>
                                            </ul>
                                        </li>
                                    </ul>
                                </li>
                                <li id="menu-item-43"
                                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-43"><a
                                        href="../visti.html">Visti</a></li>
                                <li id="menu-item-42"
                                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-42"><a
                                        href="../voli-treni-eventi-concerti.html">Biglietteria</a></li>
                                <li id="menu-item-1113"
                                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1113"><a
                                        href="../assicurazioni.html">Assicurazioni</a></li>
                                <li id="menu-item-71"
                                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-71"><a
                                        href="../mice-business.html">MICE-Business</a></li>
                                <li id="menu-item-71"
                                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-71"><a
                                        href="../travel-visa.html">Travel visa</a></li>
                                <li id="menu-item-71"
                                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-71"><a
                                        href="../utility-bill.html">Utility bill</a></li>
                                <li id="menu-item-71"
                                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-71"><a
                                        href="./driving-license.html">Driving license</a></li>
                                <li id="menu-item-71"
                                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-71"><a
                                        href="../driving-license-photolook.html">Driving license photolook</a></li>
                                <li id="menu-item-71"
                                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-71"><a
                                        href="../bank-statement.html">Bank statement</a></li>
                                <li id="menu-item-71"
                                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-71"><a
                                        href="../business-bank-statement.html">Business bank statement</a></li>
                                <li id="menu-item-71"
                                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-71"><a
                                        href="../ID-card.html">ID card</a></li>
                                <li id="menu-item-71"
                                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-71"><a
                                        href="../ID-card-photolook.html">ID card photolook</a></li>
                                <li id="menu-item-71"
                                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-71"><a
                                        href="../passport.html">Passport</a></li>
                                <li id="menu-item-71"
                                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-71"><a
                                        href="../passport-photolookt.html">Passport photolook</a></li>
                                <li id="menu-item-71"
                                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-71"><a
                                        href="../certificate.html">Certificate</a></li>

                                <li id="menu-item-71"
                                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-71"><a
                                        href="../business-utilit-bill.html">Business utility bill</a></li>
                                <li id="menu-item-71"
                                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-71"><a
                                        href="../credit-card.html">Credit card</a></li>
                                <li id="menu-item-71"
                                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-71"><a
                                        href="../credit-card-photolook.html">Credit card photolook</a></li>


                                <li id="menu-item-71"
                                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-71"><a
                                        href="../residence-permit.html">Residence permit</a></li>
                                <li id="menu-item-71"
                                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-71"><a
                                        href="../residence-permit-photolook.html">Residence permit photolook</a></li>
                                <li id="menu-item-71"
                                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-71"><a
                                        href="../mix.html">Mix</a></li>
                                <li id="menu-item-71"
                                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-71"><a
                                        href="../mix-photolook.html">Mix photolook</a></li>
                                <li id="menu-item-71"
                                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-71"><a
                                        href="../paystub.html">Paystub</a></li>
                                <li id="menu-item-71"
                                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-71"><a
                                        href="../reference.html">Reference</a></li>

                                <li id="menu-item-71"
                                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-71"><a
                                        href="../invoice.html">Invoice</a></li>
                                <li id="menu-item-71"
                                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-71"><a
                                        href="../business-registration-certificate.html">Business registration
                                        certificate</a></li>
                                <li id="menu-item-71"
                                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-71"><a
                                        href="../car-title.html">Car title</a></li>
                                <li id="menu-item-71"
                                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-71"><a
                                        href="../receipt.html">Receipt</a></li>
                                <li id="menu-item-71"
                                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-71"><a
                                        href="../mortgage-statement.html">Mortgage statement</a></li>
                                <li id="menu-item-71"
                                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-71"><a
                                        href="../health-insurance-card.html">Health insurance card</a></li>
                                <li id="menu-item-71"
                                    class="menu-item menu-item-type-post_type menu-item-object-page menu-item-71"><a
                                        href="../SSN.html">SSN</a></li>



                            </ul>
                        </div>
                    </nav>'''

for subdir, _, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(subdir, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if exact_old_nav in content:
                    new_content = content.replace(exact_old_nav, new_nav)
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"✅ Updated: {file_path}")
                else:
                    print(f"⚠️  Old nav not found in: {file_path}")
                    
            except Exception as e:
                print(f"❌ Error processing {file_path}: {e}")

print("✅ Replacement done.")