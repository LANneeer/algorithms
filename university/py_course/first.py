users_almaty = 3_500
users_astana = 4_900
revenue_almaty = 48_000
revenue_astana = 63_000

arpu_almaty = round(revenue_almaty / users_almaty, 4)
arpu_astana = round(revenue_astana / users_astana, 4)


print(
    f"Almaty: {users_almaty} users, revenue {revenue_almaty} tenge, ARPU {arpu_almaty}"
)
print(
    "Almaty: {} users, revenue {} tenge, ARPU {}".format(
        users_almaty, revenue_almaty, arpu_almaty
    )
)

print(f"Almaty is {'higher' if arpu_almaty > arpu_astana else 'lower'} than Astna")
