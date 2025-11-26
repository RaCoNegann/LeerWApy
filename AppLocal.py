import LeerMensaje
import MensajeDebug as mensajeDebug

data = {
  'object': 'whatsapp_business_account',
  'entry': [{
    'id': '2483762775358440', 
      'changes': [{
       'value': {
          'messaging_product': 'whatsapp', 
          'metadata': {
            'display_phone_number': '15551535035', 
            'phone_number_id': '845427305315318'
          }, 
        'contacts':[{
          'profile': {
            'name': 'Daniel E. Ramírez Junco'
            }, 
          'wa_id': '573202965268'
        }], 
        'messages': [{
          'from': '573202965268', 
          'id': 'wamid.HBgMNTczMjAyOTY1MjY4FQIAEhggQUMxMjQ1NUU2RjY4MkQzNzAxRTc3QUE3MkU4QTlENEMA', 
          'timestamp': '1763939819', 
          'text': {
            'body': 'graf'
          }, 
          'type': 'text'
          }]},
        'field': 'messages'
      }]
    }]
  }
#print(jsons["entry"][0]["changes"][0]["value"]["messages"][0]["text"]["body"])
archivo = "AppLocal"
try:
    texto = (data["entry"][0]["changes"][0]["value"]["messages"][0]["text"]["body"])
    numeroUsuario= data["entry"][0]["changes"][0]["value"]["messages"][0]["from"]
    mensajeDebug.mensajeConsola(archivo,"Valida mensaje",1)
    LeerMensaje.validar_mensaje(texto,numeroUsuario)
except:
    mensajeDebug.mensajeConsola(archivo,"No es mensaje de usuario",3)