for i in {1..2}
do
    echo "Running test case $i..."
    python phase3_cmdlinearg.py "Logout_test_cases/Logout_test_run_files/Logout_Input_test_run/Logout_${i}_INP.txt" "Logout_${i}_OUT.txt"
done

echo "All test cases completed."
