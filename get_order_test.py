# Нина Савотченко, 10-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data
def get_new_order_track():
    return sender_stand_request.post_new_order().json()["track"]

def get_order_status_body(track):
    current_body = data.get_order_body.copy()
    current_body["t"] = track
    return current_body

def test_get_order():
    track = get_new_order_track()
    get_order_response = sender_stand_request.get_order(get_order_status_body(track))
    assert get_order_response.status_code == 200

