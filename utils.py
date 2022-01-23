def get_round_up_number(divident, devider):
    return (int(divident / devider) + (divident % devider > 0))
