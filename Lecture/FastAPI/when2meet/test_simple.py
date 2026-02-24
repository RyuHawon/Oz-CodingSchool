from datetime import datetime, timedelta

# literal 쓰지 않고 상수를 쓰는 이유 -> 2는 배송에 걸리는 날짜임을 알아보기 위해서
# 100% 까먹으니까 2 그대로 쓰지말고 명명해서 쓰자
# magic number : 무슨 값인지 알 수 없고, 반복해서 등장하는 값. 쓰지말자.
DELIVERY_DAYS = 2


def _is_holiday(day: datetime) -> bool:
    return day.weekday() == 6
    # 0 ~ 6 : 월 ~ 일


def get_eta(purchase_date: datetime) -> datetime:
    current_date = purchase_date
    reamaining_days = DELIVERY_DAYS

    while reamaining_days > 0:
        current_date += timedelta(days=1)
        if not _is_holiday(current_date):
            reamaining_days -= 1

    return current_date


def test_get_eta_2023_12_01() -> None:
    result = get_eta(datetime(2023, 12, 1))
    assert result == datetime(2023, 12, 4)


def test_get_eta_2024_12_31() -> None:
    result = get_eta(datetime(2024, 12, 31))
    assert result == datetime(2025, 1, 2)


def test_get_eta_2024_02_28() -> None:
    result = get_eta(datetime(2024, 2, 28))
    assert result == datetime(2024, 3, 1)


def test_get_eta_2023_02_28() -> None:
    result = get_eta(datetime(2023, 2, 28))
    assert result == datetime(2023, 3, 2)
