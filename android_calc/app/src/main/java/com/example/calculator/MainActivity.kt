package com.example.calculator

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {

    private lateinit var editX: EditText
    private lateinit var editY: EditText
    private lateinit var textResult: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        editX = findViewById(R.id.editX)
        editY = findViewById(R.id.editY)
        textResult = findViewById(R.id.textResult)

        findViewById<Button>(R.id.btnAdd).setOnClickListener { calc("+") }
        findViewById<Button>(R.id.btnSub).setOnClickListener { calc("-") }
        findViewById<Button>(R.id.btnMul).setOnClickListener { calc("*") }
        findViewById<Button>(R.id.btnDiv).setOnClickListener { calc("/") }
    }

    private fun calc(op: String) {
        val x = editX.text.toString().toDoubleOrNull()
        val y = editY.text.toString().toDoubleOrNull()

        if (x == null || y == null) {
            textResult.text = "숫자를 입력하세요"
            return
        }

        val result = when (op) {
            "+" -> x + y
            "-" -> x - y
            "*" -> x * y
            "/" -> if (y == 0.0) 0.0 else x / y   // python 쪽 테스트랑 맞춰서 0으로 나누면 0
            else -> 0.0
        }

        // 정수로 떨어지면 소수점 없이 보여주기
        val text = if (result == result.toLong().toDouble()) result.toLong().toString() else result.toString()
        textResult.text = "$x $op $y = $text"
    }
}
