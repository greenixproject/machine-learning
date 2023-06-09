import os
from google.cloud import storage
from tensorflow import keras

# Inisialisasi klien Google Cloud Storage
storage_client = storage.Client.from_service_account_json('./service-account-key.json')

# Nama bucket dan folder tujuan di GCS
bucket_name = 'model_ready'
folder_name = 'model_activity'
converted_bucket_name = 'model_convert'  # Nama bucket baru untuk model yang sudah dikonversi

def upload_to_gcs(file_path):
    # Mengambil nama file dari path
    file_name = os.path.basename(file_path)

    # Mengunggah file ke GCS
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(f'{folder_name}/{file_name}')
    blob.upload_from_filename(file_path)

    print(f'File {file_name} berhasil diunggah ke GCS.')

def upload_converted_to_gcs(file_path):
    # Mengambil nama file dari path
    file_name = os.path.basename(file_path)

    # Mengunggah file ke GCS
    bucket = storage_client.get_bucket(converted_bucket_name)
    blob = bucket.blob(f'{folder_name}/{file_name}')
    blob.upload_from_filename(file_path)

    print(f'File {file_name} berhasil diunggah ke GCS.')

def convert_model(file_path):
    # Load the model
    model = keras.models.load_model(file_path)
    # Save the model to SavedModel format
    saved_model_path = file_path.replace('.h5', '')
    model.save(saved_model_path, save_format='tf')
    return saved_model_path

def search_files(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.h5'):
                file_path = os.path.join(root, file)
                saved_model_path = convert_model(file_path)
                upload_converted_to_gcs(saved_model_path)

# Menjalankan pencarian file dan mengunggahnya ke GCS
search_files(os.path.join(os.path.dirname(__file__), '..'))

def delete_obsolete_files():
    bucket = storage_client.get_bucket(bucket_name)
    blobs = bucket.list_blobs(prefix=folder_name)

    repo_files = os.listdir(os.path.join(os.path.dirname(__file__), '..'))

    for blob in blobs:
        file_name = os.path.basename(blob.name)
        if file_name not in repo_files:
            blob.delete()
            print(f'File {file_name} dihapus dari GCS.')

# Menjalankan penghapusan file yang tidak ada di repo
delete_obsolete_files()
