# Security Tools CLI Command Dataset

This dataset contains labeled command examples for training LLM models to suggest appropriate CLI commands based on natural language descriptions. **Intended for educational and authorized testing environments only.**

## Dataset Structure

Each entry contains:
- **tool**: Command-line tool name
- **nl_prompt**: Natural language description of the task
- **cli_command**: Corresponding CLI command
- **simulated_safety_note**: Usage restrictions and safety guidelines

## Tools Covered

### Network Scanning & Discovery
- **nmap**: Network exploration and security scanning

### Network Analysis
- **wireshark/tshark**: Network protocol analyzer
- **netstat**: Network connections and statistics

### Penetration Testing
- **metasploit**: Exploitation framework
- **sqlmap**: SQL injection testing tool

### Password Security
- **john**: John the Ripper password cracker
- **hydra**: Network login cracker

### Wireless Security
- **aircrack-ng**: Wireless network security suite

### Network Intrusion Detection
- **snort**: Network intrusion detection system

## Sample Entries

```csv
tool,nl_prompt,cli_command,simulated_safety_note
nmap,Scan a network range for open ports,nmap -sS 192.168.1.0/24,Demo-only. Authorized environments/labs only. No unauthorized use.
wireshark,Capture HTTP traffic on interface eth0,tshark -i eth0 -f "tcp port 80",Demo-only. Authorized environments/labs only. No unauthorized use.
john,Crack password hashes using wordlist,john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt,Demo-only. Authorized environments/labs only. No unauthorized use.
hydra,Brute force SSH login,hydra -l admin -P passwords.txt ssh://target.com,Demo-only. Authorized environments/labs only. No unauthorized use.
aircrack-ng,Crack WPA handshake,aircrack-ng -w wordlist.txt -b AA:BB:CC:DD:EE:FF capture.cap,Demo-only. Authorized environments/labs only. No unauthorized use.
```

## Training Objectives

The model should learn to:
1. Map natural language security tasks to appropriate CLI tools
2. Generate syntactically correct command structures
3. Include relevant parameters and options
4. Suggest alternative approaches when applicable
5. Always include safety disclaimers for security tools

## Usage Guidelines

### ✅ Appropriate Use
- Educational cybersecurity training
- Authorized penetration testing
- Security research in controlled environments
- Lab exercises with proper supervision

### ❌ Prohibited Use
- Unauthorized network scanning
- Attacking systems without permission
- Bypassing security controls illegally
- Any malicious or unethical activities

## Safety Considerations

- All tools included are dual-use and have legitimate security purposes
- Commands should only be executed in authorized environments
- Users must have explicit permission before running security tools
- Dataset includes safety warnings with each command suggestion
- Model training should emphasize ethical usage guidelines

## Dataset Extensions

Consider adding:
- Context-aware command parameters
- Multi-tool workflows for complex tasks
- Error handling and troubleshooting commands
- Platform-specific variations (Linux/Windows/macOS)
- Output parsing and analysis suggestions

## Legal and Ethical Notes

This dataset is designed for legitimate cybersecurity education and authorized testing only. Users are responsible for ensuring compliance with:
- Local and international laws
- Organizational policies
- Ethical hacking guidelines
- Professional codes of conduct

**Remember: With great power comes great responsibility. Use these tools ethically and legally.**
