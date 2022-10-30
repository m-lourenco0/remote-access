from flask import Blueprint, request
import pyautogui

class Remote():

    remote_controller = Blueprint('remote_controller', __name__, url_prefix='/remote')

    @remote_controller.route('/controller/press/<string:command>', methods=['POST'])
    def press(command):
        try:
            pyautogui.press(command)
            return 'Command: ' + command
        except:
            return 'Command not found'

    @remote_controller.route('/controller/hotkey/<string:command>', methods=['POST'])
    def hotkey(command):
        try:
            pyautogui.hotkey(command)
            return 'Command: ' + command
        except:
            return 'Command not found'