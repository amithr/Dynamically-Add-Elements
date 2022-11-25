import PySimpleGUI as sg

def item_row(item_num):
    row =  [sg.pin(
        sg.Col([[
            sg.Button("X", border_width=0, button_color=(sg.theme_text_color(), sg.theme_background_color()), key=('-DEL-', item_num)),
            sg.Input(size=(20,1), key=('-DESC-', item_num)),
            sg.Text(f'Row {item_num}', key=('-STATUS-', item_num))]],
        key=('-ROW-', item_num)
        ))]
    return row



layout = [  [sg.Text('Add and "Delete" Rows From a Window', font='15')],
            [sg.Column([item_row(1)], k='-ROW_PANEL-')],
            [sg.Text("X", enable_events=True, k='Exit', tooltip='Exit Application'), 
            sg.Text('+', enable_events=True, k='Add Item', tooltip='Add Another Item')]]

window = sg.Window('Dynamically Adding Elements', layout,  use_default_focus=False, font='15', metadata=1)


while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Add Item':
        window.metadata += 1
        # Allows you to add items to a layout
        # These items cannot be deleted, but can be made invisible
        window.extend_layout(window['-ROW_PANEL-'], [item_row(window.metadata)])
    elif event[0] == '-DEL-':
            window.metadata -= 1
            window[('-ROW-', event[1])].update(visible=False)
window.close()


