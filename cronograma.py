import streamlit as st
import pandas as pd

# Função principal
def main():
    st.title("Cronograma Semanal")
    st.subheader("Defina os dias, horários e atividades do seu cronograma")

    # Lista para armazenar as atividades
    if "schedule" not in st.session_state:
        st.session_state.schedule = []

    # Dias da semana
    days_of_week = [
        "Segunda-feira",
        "Terça-feira",
        "Quarta-feira",
        "Quinta-feira",
        "Sexta-feira",
        "Sábado",
        "Domingo"
    ]

    # Entrada para dia da semana, horário e atividade
    with st.form("schedule_form"):
        day = st.selectbox("Escolha o dia da semana:", days_of_week)
        time = st.time_input("Escolha o horário:")
        activity = st.text_input("Descrição da atividade:")
        submitted = st.form_submit_button("Adicionar Atividade")

        # Verifica se já existe uma atividade no mesmo dia e horário
        if submitted and activity:
            if any(item["Dia"] == day and item["Horário"] == time for item in st.session_state.schedule):
                st.error("Já existe uma atividade nesse dia e horário! Por favor, escolha outro horário.")
            else:
                st.session_state.schedule.append({"Dia": day, "Horário": time, "Atividade": activity})
                st.success("Atividade adicionada com sucesso!")

    # Botão para finalizar e exibir a tabela semanal
    if st.button("Finalizar Agenda"):
        st.success("Agenda finalizada! Abaixo está sua tabela semanal.")
        display_weekly_schedule()

# Função para exibir o cronograma como tabela semanal (colunas por dia)
def display_weekly_schedule():
    schedule_df = pd.DataFrame(st.session_state.schedule)

    if not schedule_df.empty:
        # Organiza por dia da semana e horário
        schedule_df = schedule_df.sort_values(by=["Dia", "Horário"])

        # Estrutura tabela semanal com colunas de dias da semana
        weekly_schedule = {day: [] for day in [
            "Segunda-feira", "Terça-feira", "Quarta-feira", 
            "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"
        ]}

        for day in weekly_schedule.keys():
            activities = schedule_df[schedule_df["Dia"] == day]
            weekly_schedule[day] = activities[["Horário", "Atividade"]].values.tolist()

        # Exibindo a tabela semanalhttps://www.instagram.com/dregmondalves/p/CqtMOuCSORL/
        st.write("### Tabela Semanal de Atividades")
        columns = list(weekly_schedule.keys())
        table_data = {col: [f"{entry[0]} - {entry[1]}" for entry in weekly_schedule[col]] for col in columns}
        weekly_table = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in table_data.items()]))
        st.table(weekly_table)

        # Botão de impressão
        st.button("Imprimir", on_click=print_schedule)


# Função para simular a impressão
def print_schedule():
    st.info("Use o comando de impressão do navegador (CTRL+P ou CMD+P) para imprimir a tabela.")

if __name__ == "__main__":
    main()
