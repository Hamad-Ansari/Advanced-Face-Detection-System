# Security Policy

## Supported Versions

We release patches for security vulnerabilities. Currently supported versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Reporting a Vulnerability

We take the security of Advanced Face Detection System seriously. If you believe you have found a security vulnerability, please report it to us as described below.

### Please Do Not:
- Open a public GitHub issue for security vulnerabilities
- Disclose the vulnerability publicly before it has been addressed

### Please Do:
1. **Email us directly** at mrhammadzahid24@gmail.com with:
   - Description of the vulnerability
   - Steps to reproduce the issue
   - Potential impact
   - Suggested fix (if any)

2. **Allow time for response**: We will acknowledge your email within 48 hours and provide a more detailed response within 7 days.

3. **Work with us**: We may ask for additional information or guidance.

## Security Best Practices

When using this system:

### Camera Access
- Only grant camera permissions to trusted applications
- Review camera access regularly in system settings
- Close the application when not in use

### Data Privacy
- This system processes video locally on your device
- No data is transmitted to external servers by default
- Face detection data is not stored unless explicitly saved

### Model Files
- Download models only from official sources:
  - https://github.com/opencv/opencv_extra
  - https://github.com/Hamad-Ansari/Advanced-Face-Detection-System
- Verify file integrity after download
- Keep models updated with latest versions

### Dependencies
- Regularly update dependencies: `pip install --upgrade -r requirements.txt`
- Review dependency security advisories
- Use virtual environments to isolate dependencies

### Code Execution
- Review code before running
- Don't run with elevated privileges unless necessary
- Use in controlled environments for sensitive applications

## Known Security Considerations

### Camera Access
- Application requires camera access to function
- Camera feed is processed in real-time
- No persistent storage of video data

### Model Files
- Pre-trained models are from trusted sources (OpenCV)
- Models process face images locally
- No external API calls for predictions

### Privacy
- Face detection is performed locally
- No biometric data is stored
- No network transmission of face data

## Disclosure Policy

When we receive a security bug report, we will:

1. Confirm the problem and determine affected versions
2. Audit code to find similar problems
3. Prepare fixes for all supported versions
4. Release patches as soon as possible

## Comments on this Policy

If you have suggestions on how this process could be improved, please submit a pull request or email mrhammadzahid24@gmail.com.

## Security Updates

Security updates will be announced via:
- GitHub Security Advisories
- Release notes in CHANGELOG.md
- Email to reporters

## Acknowledgments

We appreciate the security research community's efforts in responsibly disclosing vulnerabilities. Contributors who report valid security issues will be acknowledged in our release notes (unless they prefer to remain anonymous).

---

**Last Updated**: November 18, 2025
