# src/cita.py
class CitaMedica:

    def __init__(
        self,
        id_cita: str,
        paciente: str,
        especialidad: str,
        medico_asignado: str,
        costo_consulta: float,
        es_urgencia: bool,
    ):
        self.id_cita = id_cita
        self.paciente = paciente
        self.especialidad = especialidad
        self.medico_asignado = medico_asignado
        self.costo_consulta = costo_consulta
        self.es_urgencia = es_urgencia

    def calcular_costo_final(self) -> float:
        if not self.es_urgencia:
            return self.costo_consulta * 0.85
        return self.costo_consulta

    def a_diccionario(self) -> dict:
        return {
            "id_cita": self.id_cita,
            "paciente": self.paciente,
            "especialidad": self.especialidad,
            "medico_asignado": self.medico_asignado,
            "costo_consulta": self.costo_consulta,
            "es_urgencia": self.es_urgencia,
            "costo_final": self.calcular_costo_final(),
        }