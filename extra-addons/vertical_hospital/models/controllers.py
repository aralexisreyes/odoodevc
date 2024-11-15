from odoo import http
from odoo.http import request

class VerticalHospitalController(http.Controller):


    """
    Controlador para manejar las solicitudes HTTP relacionadas con los pacientes del hospital.
    """

    @http.route(route='/pacientes', type='http', auth='public', methods=['GET'])
    def get_patients(self):
        """
        Ruta para obtener la lista de todos los pacientes.

        """
        patients = request.env['vertical.hospital.patients'].search([])
        data = []  # Inicializa una lista para almacenar los datos de todos los pacientes
        for patient in patients:
            data.append({
                'seq': patient.patient_code,
                'name': patient.full_name,
                'patient_rnc': patient.patient_rnc,
                'state': patient.state
            })

        return str(data) 

    @http.route(route='/pacientes/consulta/<string:patient_code>', type='http', auth='public', methods=['GET'])
    def get_patient(self, patient_code):
        """
        Ruta para obtener los datos de un paciente específico basado en su código de paciente.
        """
        patient = request.env['vertical.hospital.patients'].search([('patient_code', '=', patient_code)], limit=1)
        
        if patient:
            data = {
                'seq': patient.patient_code,
                'name': patient.full_name,
                'patient_rnc': patient.patient_rnc,
                'state': patient.state
            }
            return str(data)
        else:
            return {"error": "Paciente no encontrado"}
