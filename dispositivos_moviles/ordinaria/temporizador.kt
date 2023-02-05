// make a temporizer that prints the time in minutes and seconds

fun main() {
    var min = 0
    var sec = 10
    var hours = 0

    print("Ingresa la cantidad de horas: ")
    hours = readLine()!!.toInt()
    print("Ingresa la cantidad de minutos: ")
    min = readLine()!!.toInt()
    print("Ingresa la cantidad de segundos: ")
    sec = readLine()!!.toInt()

    while (hours >= 0) {
        while (min >= 0) {
            while (sec >= 0) {
                val stringHours = if (hours < 10) "0$hours" else hours
                val stringMin = if (min < 10) "0$min" else min
                val stringSec = if (sec < 10) "0$sec" else sec
                println("$stringHours:$stringMin:$stringSec")
                Thread.sleep(1000L)
                sec--
            }
            sec = 59
            min--
        }
        min = 59
        hours--
    }
    println("Llegaste a la meta!")
} 