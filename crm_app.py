import streamlit as st
import pandas as pd
import os
from datetime import datetime, date, time
import json

# Sayfa yapılandırması
st.set_page_config(
    page_title="İç Mimar CRM Sistemi",
    page_icon="🏠",
    layout="wide"
)

# Dosya yolları
CSV_FILE = "interior_designer_db.csv"
APPOINTMENTS_FILE = "appointments.json"

# CSS ile stil ekleme
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .success-message {
        padding: 1rem;
        background-color: #d4edda;
        border-radius: 5px;
        color: #155724;
    }
    .error-message {
        padding: 1rem;
        background-color: #f8d7da;
        border-radius: 5px;
        color: #721c24;
    }
</style>
""", unsafe_allow_html=True)

# Veri yükleme fonksiyonları
@st.cache_data
def load_designers():
    """CSV dosyasından iç mimarları yükle"""
    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE)
        return df
    else:
        # Boş DataFrame oluştur
        return pd.DataFrame(columns=['address', 'first name', 'last name', 'phone', 'email', 'company name', 'linkedin adress'])

def save_designers(df):
    """İç mimarları CSV dosyasına kaydet"""
    df.to_csv(CSV_FILE, index=False)
    st.cache_data.clear()

def load_appointments():
    """Randevuları yükle"""
    if os.path.exists(APPOINTMENTS_FILE):
        with open(APPOINTMENTS_FILE, 'r', encoding='utf-8') as f:
            appointments = json.load(f)
        return appointments
    else:
        return []

def save_appointments(appointments):
    """Randevuları kaydet"""
    with open(APPOINTMENTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(appointments, f, ensure_ascii=False, indent=2)

# Ana başlık
st.markdown('<h1 class="main-header">🏠 İç Mimar CRM Sistemi</h1>', unsafe_allow_html=True)

# Sidebar menü
menu = st.sidebar.selectbox(
    "Menü",
    ["🏠 Ana Sayfa", "👥 İç Mimarlar", "➕ İç Mimar Ekle", "📅 Randevular", "📆 Randevu Ekle", "📊 İstatistikler", "📤 İçe/Dışa Aktar"]
)

# Ana Sayfa
if menu == "🏠 Ana Sayfa":
    st.header("Hoş Geldiniz! 👋")
    
    df = load_designers()
    appointments = load_appointments()
    
    # İstatistik kartları
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Toplam İç Mimar", len(df))
    
    with col2:
        st.metric("Toplam Randevu", len(appointments))
    
    with col3:
        # Bugünkü randevular
        today = date.today().isoformat()
        today_appointments = [a for a in appointments if a.get('date') == today]
        st.metric("Bugünkü Randevular", len(today_appointments))
    
    st.markdown("---")
    
    # Son eklenen iç mimarlar
    st.subheader("📋 Son Eklenen İç Mimarlar")
    if len(df) > 0:
        st.dataframe(df.tail(5), use_container_width=True)
    else:
        st.info("Henüz iç mimar eklenmemiş.")
    
    st.markdown("---")
    
    # Yaklaşan randevular
    st.subheader("📅 Yaklaşan Randevular")
    if len(appointments) > 0:
        # Tarihe göre sırala
        sorted_appointments = sorted(appointments, key=lambda x: (x.get('date', ''), x.get('time', '')))
        upcoming = [a for a in sorted_appointments if a.get('date', '') >= date.today().isoformat()][:5]
        
        if upcoming:
            for apt in upcoming:
                with st.expander(f"📌 {apt.get('date')} - {apt.get('time')} | {apt.get('designer_name', 'N/A')}"):
                    st.write(f"**Müşteri:** {apt.get('client_name', 'N/A')}")
                    st.write(f"**Telefon:** {apt.get('client_phone', 'N/A')}")
                    st.write(f"**Notlar:** {apt.get('notes', 'Yok')}")
        else:
            st.info("Yaklaşan randevu bulunmuyor.")
    else:
        st.info("Henüz randevu eklenmemiş.")

# İç Mimarlar Sayfası
elif menu == "👥 İç Mimarlar":
    st.header("👥 İç Mimarlar Listesi")
    
    df = load_designers()
    
    if len(df) > 0:
        # Arama ve filtreleme
        col1, col2 = st.columns([2, 1])
        
        with col1:
            search_term = st.text_input("🔍 Ara (İsim, Şirket, Email)", "")
        
        with col2:
            st.write("")  # Boşluk için
        
        # Filtreleme
        if search_term:
            mask = df.apply(lambda row: row.astype(str).str.contains(search_term, case=False, na=False).any(), axis=1)
            filtered_df = df[mask]
        else:
            filtered_df = df
        
        st.success(f"Toplam {len(filtered_df)} iç mimar bulundu")
        
        # Tablo gösterimi
        st.dataframe(filtered_df, use_container_width=True)
        
        st.markdown("---")
        
        # İç mimar silme
        st.subheader("🗑️ İç Mimar Sil")
        
        # İsim listesi oluştur
        designer_names = []
        for idx, row in df.iterrows():
            name = f"{row['first name']} {row['last name']} - {row['company name']}"
            designer_names.append((idx, name))
        
        selected_designer = st.selectbox(
            "Silmek istediğiniz iç mimarı seçin:",
            options=[idx for idx, name in designer_names],
            format_func=lambda idx: designer_names[idx][1] if idx < len(designer_names) else ""
        )
        
        col1, col2, col3 = st.columns([1, 1, 2])
        
        with col1:
            if st.button("🗑️ Sil", type="primary"):
                df = df.drop(selected_designer).reset_index(drop=True)
                save_designers(df)
                st.success("✅ İç mimar başarıyla silindi!")
                st.rerun()
        
        with col2:
            if st.button("🔄 Yenile"):
                st.rerun()
    else:
        st.warning("Henüz iç mimar bulunmuyor. Lütfen iç mimar ekleyin.")

# İç Mimar Ekle Sayfası
elif menu == "➕ İç Mimar Ekle":
    st.header("➕ Yeni İç Mimar Ekle")
    
    with st.form("add_designer_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            first_name = st.text_input("Ad *")
            last_name = st.text_input("Soyad *")
            email = st.text_input("Email")
            phone = st.text_input("Telefon")
        
        with col2:
            company_name = st.text_input("Şirket Adı *")
            address = st.text_input("Adres")
            linkedin = st.text_input("LinkedIn Adresi")
        
        st.markdown("**\* Zorunlu alanlar**")
        
        submitted = st.form_submit_button("✅ Ekle", type="primary")
        
        if submitted:
            if not first_name or not last_name or not company_name:
                st.error("❌ Lütfen zorunlu alanları doldurun!")
            else:
                df = load_designers()
                
                new_designer = {
                    'address': address,
                    'first name': first_name,
                    'last name': last_name,
                    'phone': phone,
                    'email': email,
                    'company name': company_name,
                    'linkedin adress': linkedin
                }
                
                df = pd.concat([df, pd.DataFrame([new_designer])], ignore_index=True)
                save_designers(df)
                
                st.success(f"✅ {first_name} {last_name} başarıyla eklendi!")
                st.balloons()

# Randevular Sayfası
elif menu == "📅 Randevular":
    st.header("📅 Randevu Takvimi")
    
    appointments = load_appointments()
    
    # Takvim görünümü için tarih seçimi
    col1, col2 = st.columns([2, 1])
    
    with col1:
        selected_date = st.date_input("📆 Tarih Seçin", value=date.today())
    
    with col2:
        view_type = st.radio("Görünüm", ["Günlük", "Haftalık", "Tümü"])
    
    # Randevuları filtrele
    if view_type == "Günlük":
        filtered_appointments = [a for a in appointments if a.get('date') == selected_date.isoformat()]
        st.subheader(f"📅 {selected_date.strftime('%d.%m.%Y')} Tarihli Randevular")
    elif view_type == "Haftalık":
        from datetime import timedelta
        week_start = selected_date - timedelta(days=selected_date.weekday())
        week_end = week_start + timedelta(days=6)
        filtered_appointments = [a for a in appointments if week_start.isoformat() <= a.get('date', '') <= week_end.isoformat()]
        st.subheader(f"📅 {week_start.strftime('%d.%m.%Y')} - {week_end.strftime('%d.%m.%Y')} Randevular")
    else:
        filtered_appointments = sorted(appointments, key=lambda x: (x.get('date', ''), x.get('time', '')))
        st.subheader("📅 Tüm Randevular")
    
    if filtered_appointments:
        st.success(f"Toplam {len(filtered_appointments)} randevu bulundu")
        
        for idx, apt in enumerate(filtered_appointments):
            with st.expander(f"🕐 {apt.get('date')} - {apt.get('time')} | İç Mimar: {apt.get('designer_name', 'N/A')}"):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write(f"**👤 Müşteri:** {apt.get('client_name', 'N/A')}")
                    st.write(f"**📞 Telefon:** {apt.get('client_phone', 'N/A')}")
                    st.write(f"**📧 Email:** {apt.get('client_email', 'N/A')}")
                
                with col2:
                    st.write(f"**🏠 İç Mimar:** {apt.get('designer_name', 'N/A')}")
                    st.write(f"**📍 Adres:** {apt.get('location', 'N/A')}")
                    st.write(f"**📝 Notlar:** {apt.get('notes', 'Yok')}")
                
                if st.button(f"🗑️ Randevuyu Sil", key=f"delete_{idx}"):
                    appointments.remove(apt)
                    save_appointments(appointments)
                    st.success("✅ Randevu silindi!")
                    st.rerun()
    else:
        st.info("Bu tarihte randevu bulunmuyor.")

# Randevu Ekle Sayfası
elif menu == "📆 Randevu Ekle":
    st.header("📆 Yeni Randevu Ekle")
    
    df = load_designers()
    
    if len(df) > 0:
        with st.form("add_appointment_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("📅 Randevu Bilgileri")
                appointment_date = st.date_input("Tarih *", value=date.today())
                appointment_time = st.time_input("Saat *", value=time(9, 0))
                
                # İç mimar seçimi
                designer_options = [f"{row['first name']} {row['last name']} - {row['company name']}" for idx, row in df.iterrows()]
                selected_designer = st.selectbox("İç Mimar Seçin *", options=designer_options)
                
                location = st.text_input("Randevu Yeri")
            
            with col2:
                st.subheader("👤 Müşteri Bilgileri")
                client_name = st.text_input("Müşteri Adı *")
                client_phone = st.text_input("Müşteri Telefon *")
                client_email = st.text_input("Müşteri Email")
                notes = st.text_area("Notlar", height=100)
            
            st.markdown("**\* Zorunlu alanlar**")
            
            submitted = st.form_submit_button("✅ Randevu Ekle", type="primary")
            
            if submitted:
                if not client_name or not client_phone or not selected_designer:
                    st.error("❌ Lütfen zorunlu alanları doldurun!")
                else:
                    appointments = load_appointments()
                    
                    new_appointment = {
                        'date': appointment_date.isoformat(),
                        'time': appointment_time.strftime("%H:%M"),
                        'designer_name': selected_designer,
                        'client_name': client_name,
                        'client_phone': client_phone,
                        'client_email': client_email,
                        'location': location,
                        'notes': notes,
                        'created_at': datetime.now().isoformat()
                    }
                    
                    appointments.append(new_appointment)
                    save_appointments(appointments)
                    
                    st.success(f"✅ Randevu başarıyla eklendi!")
                    st.balloons()
    else:
        st.warning("⚠️ Randevu eklemek için önce iç mimar eklemelisiniz!")
        if st.button("➕ İç Mimar Ekle"):
            st.switch_page("pages/add_designer.py")

# İstatistikler Sayfası
elif menu == "📊 İstatistikler":
    st.header("📊 İstatistikler ve Raporlar")
    
    df = load_designers()
    appointments = load_appointments()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("👥 İç Mimar İstatistikleri")
        st.metric("Toplam İç Mimar", len(df))
        
        if len(df) > 0:
            # Email olan/olmayan
            with_email = df['email'].notna().sum()
            without_email = len(df) - with_email
            
            st.write("**Email İstatistikleri:**")
            st.write(f"- Email olan: {with_email}")
            st.write(f"- Email olmayan: {without_email}")
            
            # Telefon olan/olmayan
            with_phone = df['phone'].notna().sum()
            without_phone = len(df) - with_phone
            
            st.write("**Telefon İstatistikleri:**")
            st.write(f"- Telefon olan: {with_phone}")
            st.write(f"- Telefon olmayan: {without_phone}")
    
    with col2:
        st.subheader("📅 Randevu İstatistikleri")
        st.metric("Toplam Randevu", len(appointments))
        
        if len(appointments) > 0:
            # Bugünkü randevular
            today = date.today().isoformat()
            today_appointments = [a for a in appointments if a.get('date') == today]
            
            # Geçmiş randevular
            past_appointments = [a for a in appointments if a.get('date', '') < today]
            
            # Gelecek randevular
            future_appointments = [a for a in appointments if a.get('date', '') > today]
            
            st.write("**Randevu Dağılımı:**")
            st.write(f"- Bugün: {len(today_appointments)}")
            st.write(f"- Geçmiş: {len(past_appointments)}")
            st.write(f"- Gelecek: {len(future_appointments)}")
    
    st.markdown("---")
    
    # En çok randevusu olan iç mimarlar
    if len(appointments) > 0:
        st.subheader("🏆 En Çok Randevusu Olan İç Mimarlar")
        
        designer_counts = {}
        for apt in appointments:
            designer = apt.get('designer_name', 'Bilinmiyor')
            designer_counts[designer] = designer_counts.get(designer, 0) + 1
        
        sorted_designers = sorted(designer_counts.items(), key=lambda x: x[1], reverse=True)[:5]
        
        for idx, (designer, count) in enumerate(sorted_designers, 1):
            st.write(f"{idx}. {designer}: **{count}** randevu")

# İçe/Dışa Aktar Sayfası
elif menu == "📤 İçe/Dışa Aktar":
    st.header("📤 İçe/Dışa Aktar")
    
    tab1, tab2, tab3 = st.tabs(["📥 CSV İçe Aktar", "📤 CSV Dışa Aktar", "📋 Boş Şablon İndir"])
    
    # CSV İçe Aktar
    with tab1:
        st.subheader("📥 CSV Dosyası İçe Aktar")
        st.info("Mevcut verilerinize yeni iç mimarlar eklemek için CSV dosyası yükleyin.")
        
        uploaded_file = st.file_uploader("CSV dosyası seçin", type=['csv'])
        
        if uploaded_file is not None:
            try:
                # Önizleme
                uploaded_df = pd.read_csv(uploaded_file)
                
                st.success(f"✅ Dosya başarıyla yüklendi! {len(uploaded_df)} kayıt bulundu.")
                
                st.write("**Önizleme:**")
                st.dataframe(uploaded_df.head(10), use_container_width=True)
                
                col1, col2 = st.columns(2)
                
                with col1:
                    if st.button("✅ İçe Aktar (Ekle)", type="primary"):
                        df = load_designers()
                        # Mevcut verilere ekle
                        combined_df = pd.concat([df, uploaded_df], ignore_index=True)
                        save_designers(combined_df)
                        st.success(f"✅ {len(uploaded_df)} yeni kayıt eklendi!")
                        st.balloons()
                        st.rerun()
                
                with col2:
                    if st.button("🔄 İçe Aktar (Değiştir)", type="secondary"):
                        # Tüm veriyi değiştir
                        save_designers(uploaded_df)
                        st.success(f"✅ Veriler güncellendi! Toplam {len(uploaded_df)} kayıt.")
                        st.balloons()
                        st.rerun()
                
            except Exception as e:
                st.error(f"❌ Dosya okunurken hata oluştu: {str(e)}")
                st.info("Lütfen CSV dosyasının doğru formatta olduğundan emin olun.")
    
    # CSV Dışa Aktar
    with tab2:
        st.subheader("📤 Verileri CSV Olarak Dışa Aktar")
        
        df = load_designers()
        
        if len(df) > 0:
            st.info(f"Toplam {len(df)} iç mimar kaydı mevcut.")
            
            # CSV'ye dönüştür
            csv_data = df.to_csv(index=False).encode('utf-8')
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.download_button(
                    label="📥 Tüm Verileri İndir (CSV)",
                    data=csv_data,
                    file_name=f"ic_mimarlar_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv",
                    type="primary"
                )
            
            with col2:
                # Filtrelenmiş veri indirme
                st.write("**Filtreleme Seçenekleri:**")
                
            # Email olmayanları filtrele
            if st.checkbox("Sadece email adresi olanlar"):
                df = df[df['email'].notna()]
            
            if st.checkbox("Sadece telefon numarası olanlar"):
                df = df[df['phone'].notna()]
            
            if len(df) > 0 and (st.session_state.get('filtered', False)):
                filtered_csv = df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="📥 Filtrelenmiş Verileri İndir",
                    data=filtered_csv,
                    file_name=f"ic_mimarlar_filtreli_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv"
                )
            
            st.markdown("---")
            st.write("**Önizleme:**")
            st.dataframe(df.head(10), use_container_width=True)
            
        else:
            st.warning("Henüz dışa aktarılacak veri yok.")
    
    # Boş Şablon İndir
    with tab3:
        st.subheader("📋 Boş CSV Şablonu İndir")
        
        st.info("Bu şablonu kullanarak toplu iç mimar ekleyebilirsiniz.")
        
        # Boş şablon oluştur
        template_df = pd.DataFrame(columns=['address', 'first name', 'last name', 'phone', 'email', 'company name', 'linkedin adress'])
        
        # Örnek satır ekle
        example_row = {
            'address': '123 Main St, New York',
            'first name': 'John',
            'last name': 'Doe',
            'phone': '+1 234 567 8900',
            'email': 'john@example.com',
            'company name': 'Example Design Co.',
            'linkedin adress': 'https://linkedin.com/in/johndoe'
        }
        
        template_with_example = pd.concat([template_df, pd.DataFrame([example_row])], ignore_index=True)
        
        st.write("**Şablon Formatı:**")
        st.dataframe(template_with_example, use_container_width=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Boş şablon
            empty_csv = template_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Boş Şablon İndir",
                data=empty_csv,
                file_name="ic_mimar_sablon_bos.csv",
                mime="text/csv",
                type="primary"
            )
        
        with col2:
            # Örnek içeren şablon
            example_csv = template_with_example.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Örnek Şablon İndir",
                data=example_csv,
                file_name="ic_mimar_sablon_ornek.csv",
                mime="text/csv"
            )
        
        st.markdown("---")
        
        st.write("**📝 Kullanım Talimatları:**")
        st.markdown("""
        1. Yukarıdaki butonlardan birini kullanarak şablon dosyasını indirin
        2. Excel, Google Sheets veya herhangi bir metin editörü ile açın
        3. Gerekli bilgileri doldurun (first name, last name ve company name zorunludur)
        4. Dosyayı CSV formatında kaydedin
        5. "📥 CSV İçe Aktar" sekmesinden dosyayı yükleyin
        
        **⚠️ Önemli Notlar:**
        - Sütun başlıklarını değiştirmeyin
        - Türkçe karakter kullanabilirsiniz
        - Email ve telefon alanları opsiyoneldir
        - Her satır bir iç mimara karşılık gelir
        """)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666; padding: 1rem;'>
        <p>🏠 İç Mimar CRM Sistemi | © 2025</p>
    </div>
    """,
    unsafe_allow_html=True
)