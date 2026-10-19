def add_gold(current_gold: int, reward: int) -> int:
    """Дайсны шагналыг gold-д нэмнэ; сөрөг утгыг зөвшөөрөхгүй."""
    if current_gold < 0 or reward < 0:
        raise ValueError("Gold болон reward сөрөг байж болохгүй")
    return current_gold + reward