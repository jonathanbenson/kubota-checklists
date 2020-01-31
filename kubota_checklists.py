
serials = list()

while True :

	try :

		serials.append(int(input("Enter number or -1 when done: ")))

		if serials[-1] < 0 :

			serials.pop(-1)
			break

	except ValueError :

		print("Error. Enter an integer.")


serials.sort()


outsiders = list()
repeats = list()
lost = list()

min_serial = int(input("Enter in minimum serial: "))
max_serial = int(input("Enter in maximum serial: "))

for serial in serials[:] :

    if serial > max_serial or serial < min_serial :

        outsiders.append(serial)

        serials.remove(serial)

serials_copy = serials[:]

for i in range(len(serials_copy)) :

	if i != len(serials_copy) - 1 and serials_copy[i + 1] == serials_copy[i] :

		repeats.append(serials_copy[i])

		serials.remove(serials_copy[i])


current_serial = min_serial

while current_serial <= max_serial :

	if current_serial not in serials :

		lost.append(current_serial)

	current_serial += 1


outsiders = [str(e) for e in outsiders]
repeats = [str(e) for e in repeats]
lost = [str(e) for e in lost]


print("Outsiders: {}".format(",".join(outsiders)))
print("Repeats: {}".format(",".join(repeats)))
print("Lost: {}".format(",".join(lost)))



