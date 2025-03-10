for i in {1..7}
do
    echo "Running test case $i..."
    python phase3_cmdlinearg.py "Login_test_cases/Login_test_run_files/Login_Input_test_run/Login_${i}_INP.txt" "Login_${i}_OUT.txt"
done

echo "All test cases completed."
