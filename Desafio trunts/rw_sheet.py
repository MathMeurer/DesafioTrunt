from googleapiclient.discovery import build

from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '1cuo59MW4BqSetF5bvOgiopSJK0RMObVFIz0asPe7SRk'
# O ID spreadsheet, onde foi posto o link da planilha utilizada no programa
creds = None
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

def read_sheets(where_read):
    service = build('sheets', 'v4', credentials=creds)
    # Chama o Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=where_read).execute()
    values = result.get('values', [])
    return values

sample = [[""]]

def write_final_result(to_write = sample):
    service = build('sheets', 'v4', credentials=creds)
    # Chama o Sheets API
    sheet = service.spreadsheets()
    request = sheet.values().update(spreadsheetId=SPREADSHEET_ID, range="engenharia_de_software!G4:H27", 
                                valueInputOption="USER_ENTERED", body={"values": to_write}).execute()
    return "ok"
#utilizado definir onde vai ser escrito o resultado no sheets, local = range, forma = ValueinputOption = USER_ENTERED (valores que ja estao na planilha) e body= valores a serem escritos
