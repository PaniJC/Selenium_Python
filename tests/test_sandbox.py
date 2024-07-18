import pytest
import allure

@allure.title(
    "Al dar clic en enviar, debe aparecer un texto 3 segundos después, conteniendo en el valor lo siguiente 'OMG, aparezco después de 3 segundos de haber hecho click en el botón'."
)
@allure.epic("Interfaz Web")
@allure.feature("Buttons")
@allure.story("Validación de actividades dinámicas sobre los botones.")
@allure.testcase("IS-137")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link(
    "https://logic-valere.atlassian.net/browse/PAIE-18?atlOrigin=eyJpIjoiOWI5MWM4ZTAwOGM2NGUzMWE1ZGViMTFhODE0MmE1OWMiLCJwIjoiaiJ9"
)
@pytest.mark.regression
def test_click_en_enviar(sandbox_page):
        sandbox_page.navigate_sandbox()
        sandbox_page.click_enviar()
        sandbox_page.click_boton_id_dinamico()
        
        # Estamos aplicando la espera EXPLICITA a que el elemento sea visible.
        elemento_texto_oculto = sandbox_page.wait_for_element(sandbox_page.HIDDEN_TEXT_LABEL)
        
        # Creamos la variable con el texto esperado y hacemos el assertion
        texto_esperado = ('OMG, aparezco después de 3 segundos de haber hecho click en el botón')
        try:
            assert(
                texto_esperado in elemento_texto_oculto.text
            ), "El texto esperado NO coincide con el texto encontrado"
            
        except AssertionError as e:
                print(f"Test failed with assertion error: {e}")
                raise


@allure.title(
    "El botón con id dinámico debe cambiar de color al desplazar el mouse sobre el (Hover)."
)
@allure.epic("Interfaz Web")
@allure.feature("Buttons")
@allure.story("Validación de actividades dinámicas sobre los botones.")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link(
    "https://logic-valere.atlassian.net/browse/PAIE-18?atlOrigin=eyJpIjoiOWI5MWM4ZTAwOGM2NGUzMWE1ZGViMTFhODE0MmE1OWMiLCJwIjoiaiJ9"
)
@pytest.mark.regression
def test_boton_id_dinamico_cambia_color_al_hacer_hover(sandbox_page):
        with allure.step(
            "Dado a que navego al Sandbox de Free Range Testers, capturo el background color del botón dinámico, antes de hacerle hover"
        ):
            sandbox_page.navigate_sandbox()
            boton_id_dinamico = sandbox_page.wait_for_element(sandbox_page.DYNAMIC_ID_BUTTON)
            color_before_hover = boton_id_dinamico.value_of_css_property("background-color")

        with allure.step(
            "Y cuando capturo el background color del botón dinámico, antes de hacerle hover"
        ):
            sandbox_page.hover_over_dynamic_id_button()
            color_after_hover = boton_id_dinamico.value_of_css_property("background-color")
        
        with allure.step(
            "Puedo verificar que el color antes del Hover y después del Hover sean distintos."
        ):
            try:
                assert color_before_hover != color_after_hover
            
            except AssertionError as e:
                 print(f"Test failed with assertion error: {e}")
                 raise

  
@allure.title(
    "Podemos asociar el checkbox a un alimento en el componente opción de comida."
)
@allure.epic("Interfaz Web")
@allure.feature("Elementos del Chcekbox")
@allure.story("Elección de una opción en los Checkbox de la sección.")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link(
    "https://logic-valere.atlassian.net/browse/PAIE-18?atlOrigin=eyJpIjoiOWI5MWM4ZTAwOGM2NGUzMWE1ZGViMTFhODE0MmE1OWMiLCJwIjoiaiJ9"
)
@pytest.mark.regression 
def test_elegir_checkbox(sandbox_page):
        label_text = "Hamburguesa"
        with allure.step(
            "Dado a que navego al Sandbox de Free Range Testers,"
        ):
            sandbox_page.navigate_sandbox()
            
        with allure.step(
            "Puedo seleccionar un alimento dando click al checkbox asociado a el."
        ):
            sandbox_page.select_checkbox_with_label(label_text)
            
            try:
                assert sandbox_page.is_checkbox_selected(label_text), f"El checkbox no está seleccionado '{label_text}' al hacerle click"
                
            except AssertionError as e:
                 print(f"Test failed with assertion error: {e}")
                 raise
    
    
@allure.title(
    "La opción 'No' del RadioButton debe ser seleccionada."
)
@allure.epic("Interfaz Web")
@allure.feature("Elementos del RadioButton")
@allure.story("Elección de una opción en los RadioButton de la sección.")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link(
    "https://logic-valere.atlassian.net/browse/PAIE-18?atlOrigin=eyJpIjoiOWI5MWM4ZTAwOGM2NGUzMWE1ZGViMTFhODE0MmE1OWMiLCJwIjoiaiJ9"
)
@pytest.mark.regression 
def test_elegir_radio_button(sandbox_page):
        option_radio_button = "No"
        with allure.step(
            "Dado a que navego al Sandbox de Free Range Testers y selecciono el Radio Button que dice {option_radio_button}"
        ):
            sandbox_page.navigate_sandbox()
            sandbox_page.select_radio_button(option_radio_button)
            
        with allure.step(
            "Puedo verificar que el button '{option_radio_button}' ha sido seleccionado correctamente."
        ):
            try:
                assert (
                    sandbox_page.is_radio_button_selected(
                        option_radio_button
                    ), f"El radio button '{option_radio_button}' no está seleccionado."
                )
            
            except AssertionError as e:
                 print(f"Test failed with assertion error: {e}")
                 raise


@allure.title(
    "El dropdown debe contener el valor 'Tennis' en su lista, y debe dejarse seleccionar"
)
@allure.epic("Interfaz Web")
@allure.feature("Elementos de Dropdown")
@allure.story("Elección de una opción de la lista del Dropdown.")
@allure.severity(allure.severity_level.TRIVIAL)
@allure.link(
    "https://logic-valere.atlassian.net/browse/PAIE-18?atlOrigin=eyJpIjoiOWI5MWM4ZTAwOGM2NGUzMWE1ZGViMTFhODE0MmE1OWMiLCJwIjoiaiJ9"
)
@pytest.mark.regression 
def test_elegir_deporte_del_dropdown(sandbox_page):
        with allure.step(
            "Dado a que navego al Sandbox de Free Range Testers,"
        ):
            sandbox_page.navigate_sandbox()

        with allure.step(
            "Puedo validar que la opción que estoy tratando de seleccionar sea correcta.."
        ):
            try:
                sandbox_page.select_deporte('Tennis')
                
            except Exception as e:
                 print(f"Test failed with assertion error: {e}")
                 raise


  
@allure.title(
    "El dropdown debe contener los valores 'Seleccioná un deporte,Fútbol,Tennis y Basketball'"
)
@allure.epic("Interfaz Web")
@allure.feature("Elementos de Dropdown")
@allure.story("Validación de elementos del Dropdown iguales a los establecidos.")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link(
    "https://logic-valere.atlassian.net/browse/PAIE-18?atlOrigin=eyJpIjoiOWI5MWM4ZTAwOGM2NGUzMWE1ZGViMTFhODE0MmE1OWMiLCJwIjoiaiJ9"
)
@pytest.mark.regression
def test_sports_dropdown_options(sandbox_page):
        with allure.step(
            "Dado a que navego al Sandbox de Free Range Testers y doy click al popup button."
        ):
            sandbox_page.navigate_sandbox()

        with allure.step(
            "Cuando capturo las opciones que contiene el dropdown"
        ):
            options = sandbox_page.get_sports_dropdown_options()
            
        with allure.step(
            "Puedo verificar que corresponden a las correctas"
        ):
            expected_options = ["Seleccioná un deporte","Fútbol","Tennis","Basketball"]
        try:
            assert all(
                option in options for option in expected_options
            ), "No todas las opciones esperadas son las mismas"
            
        except AssertionError as e:
                print(f"Test failed with assertion error: {e}")
                raise



@allure.title(
    "El valor del título del Popup debe ser igual a 'Popup de ejemplo'"
)
@allure.epic("Interfaz Web")
@allure.feature("Título Popup")
@allure.story("Validación de texto en título.")
@allure.severity(allure.severity_level.MINOR)
@allure.link(
    "https://logic-valere.atlassian.net/browse/PAIE-18?atlOrigin=eyJpIjoiOWI5MWM4ZTAwOGM2NGUzMWE1ZGViMTFhODE0MmE1OWMiLCJwIjoiaiJ9"
)
@pytest.mark.regression 
def test_popup_title(sandbox_page):
        with allure.step(
            "Dado a que navego al Sandbox de Free Range Testers y doy click al popup button."
        ):
            sandbox_page.navigate_sandbox()
            sandbox_page.click_popup_button()

        with allure.step(
            "Cuando capturo el texto de la ventana que emerge (Popup)"
        ):
            popup_title_text = sandbox_page.get_popup_title_text()
            expected_popup_text = "Popup de ejemplo"
        with allure.step(
            "Puedo verificar que efectivamente el título es el esperado 'Popup de ejemplo'"
        ):
            try:    
                assert (
                    popup_title_text==expected_popup_text
                    ), f"El título del Popup NO es el esperado; se obtuvo '{popup_title_text}'"
            except AssertionError as e:
                 print(f"Test failed with assertion error: {e}")
                 raise
            

@allure.title(
    "El valor de las celdas SI cambia cuando hay una recarga de la página para la tabla dinámica."
)
@allure.epic("Interfaz Web")
@allure.feature("Tabla dinámica")
@allure.story("Comportamiento Celdas")
@allure.severity(allure.severity_level.NORMAL)
@allure.link(
    "https://logic-valere.atlassian.net/browse/PAIE-18?atlOrigin=eyJpIjoiOWI5MWM4ZTAwOGM2NGUzMWE1ZGViMTFhODE0MmE1OWMiLCJwIjoiaiJ9"
)
@pytest.mark.regression
def test_cell_value_change_post_reload(sandbox_page):
        with allure.step(
            "Dado que navego al sandbox de Free Range Testers y tomo como referencia una celda de la tabla dinámica"
        ):
            sandbox_page.navigate_sandbox()
            expected_cell_value = sandbox_page.get_cell_value(3, 3)
            
        with allure.step(
            "Cuándo hago una recarga de la página y tomo el valor de la misma celda"
        ):
            sandbox_page.reload_page()
            new_cell_value = sandbox_page.get_cell_value(3, 3)
            
        with allure.step(
            "Puedo verificar que efectivamente el valor NO se modificó con la recarga de la página"
        ):   
            try: 
                assert (
                    expected_cell_value != new_cell_value
                ), f"El valor de la celda es igual a la que tenía antes de la recarga. Tenía el '{expected_cell_value}' y al recargar, trajo el '{new_cell_value}'"
            
            except AssertionError as e:
                 print(f"Test failed with assertion error: {e}")
                 raise
    
    
@allure.title(
    "El valor de las celdas NO cambia cuando hay una recarga de la página para la tabla estática"
)
@allure.epic("Interfaz Web")
@allure.feature("Tabla estática")
@allure.story("Comportamiento Celdas")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link(
    "https://logic-valere.atlassian.net/browse/PAIE-18?atlOrigin=eyJpIjoiOWI5MWM4ZTAwOGM2NGUzMWE1ZGViMTFhODE0MmE1OWMiLCJwIjoiaiJ9"
)
@pytest.mark.regression    
def test_cell_value_change_post_reload_static(sandbox_page):
        with allure.step(
            "Dado que navego al sandbox de Free Range Testers y tomo como referencia una celda de la tabla estática"
        ):
            sandbox_page.navigate_sandbox()
            expected_cell_value = sandbox_page.get_cell_value_static(2, 2)
            
        with allure.step(
            "Cuándo hago una recarga de la página y tomo el valor de la misma celda"
        ):
            sandbox_page.reload_page()
            new_cell_value = sandbox_page.get_cell_value_static(2, 2)
            
        with allure.step(
            "Puedo verificar que efectivamente el valor NO se modificó con la recarga de la página"
        ):
            try:
                assert (
                    expected_cell_value == new_cell_value
                ), f"El valor de la celda es diferente a la que tenía antes de la recarga. Tenía el '{expected_cell_value}' y al recargar, trajo el '{new_cell_value}'"

            except AssertionError as e:
                 print(f"Test failed with assertion error: {e}")
                 raise     


    
    